"""Rutas HTTP del dominio de evaluación — cuestionario, sesiones y
resultados. Prototipo sintético (D-14): ver docs/01 y docs/02 para los
límites de interpretación y uso."""

from __future__ import annotations

import datetime as dt
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as OrmSession

from app.assessment.models import AssessmentVersion, Question, Response, TestSession
from app.assessment.schemas import (
    AffinityOut,
    AssessmentRef,
    DomainScoreOut,
    QuestionList,
    QuestionOut,
    ResultOut,
    SessionCreate,
)
from app.assessment.service import (
    EXPLORATION_PROMPTS,
    LIMITATIONS_TEXT,
    compute_affinities,
    resolve_assessment_version,
    score_domains,
)
from app.catalog.models import CatalogVersion, Program
from app.catalog.schemas import CatalogRef
from app.catalog.service import resolve_version
from app.core.db import get_session

router = APIRouter(tags=["assessment"])

Db = Annotated[OrmSession, Depends(get_session)]


def _to_result_out(session: TestSession, assessment: AssessmentVersion, catalog: CatalogVersion) -> ResultOut:
    return ResultOut(
        session_id=session.id,
        assessment=AssessmentRef.model_validate(assessment),
        catalog=CatalogRef.model_validate(catalog),
        submitted_at=session.submitted_at,
        domain_scores=[DomainScoreOut(**d) for d in session.domain_scores],
        affinities=[AffinityOut(**a) for a in session.affinities],
        limitations=LIMITATIONS_TEXT,
        exploration_prompts=EXPLORATION_PROMPTS,
    )


@router.get("/assessment/versions", response_model=list[AssessmentRef])
def list_assessment_versions(db: Db) -> list[AssessmentVersion]:
    return list(db.scalars(select(AssessmentVersion).order_by(AssessmentVersion.created_at.desc())))


@router.get("/assessment/questions", response_model=QuestionList)
def list_questions(
    db: Db,
    assessment: Annotated[str | None, Query(description="Etiqueta de versión")] = None,
) -> QuestionList:
    version = resolve_assessment_version(db, assessment)
    questions = list(
        db.scalars(
            select(Question).where(Question.assessment_version_id == version.id).order_by(Question.id)
        )
    )
    return QuestionList(
        assessment=AssessmentRef.model_validate(version),
        questions=[QuestionOut(id=q.id, text=q.text, domain_code=q.domain.code) for q in questions],
    )


@router.post("/assessment/sessions", response_model=ResultOut)
def create_session(body: SessionCreate, db: Db) -> ResultOut:
    assessment = resolve_assessment_version(db, body.assessment)
    catalog = resolve_version(db, body.catalog)

    questions = list(
        db.scalars(select(Question).where(Question.assessment_version_id == assessment.id))
    )
    expected_ids = {q.id for q in questions}
    received_ids = {r.question_id for r in body.responses}
    if received_ids != expected_ids:
        raise HTTPException(
            400, "Las respuestas deben cubrir exactamente todas las preguntas del cuestionario."
        )

    responses_by_question_id = {r.question_id: r.value for r in body.responses}
    domain_scores = score_domains(questions, responses_by_question_id)

    programs = list(db.scalars(select(Program).where(Program.catalog_version_id == catalog.id)))
    affinities = compute_affinities(db, domain_scores, programs)

    session = TestSession(
        assessment_version_id=assessment.id,
        catalog_version_id=catalog.id,
        submitted_at=dt.datetime.utcnow(),
        domain_scores=domain_scores,
        affinities=affinities,
    )
    db.add(session)
    db.flush()
    db.add_all(
        Response(session_id=session.id, question_id=qid, value=value)
        for qid, value in responses_by_question_id.items()
    )
    db.commit()

    return _to_result_out(session, assessment, catalog)


@router.get("/assessment/sessions/{session_id}", response_model=ResultOut)
def get_session(session_id: str, db: Db) -> ResultOut:
    session = db.get(TestSession, session_id)
    if session is None:
        raise HTTPException(404, f"La sesión '{session_id}' no existe.")
    assessment = db.get(AssessmentVersion, session.assessment_version_id)
    catalog = db.get(CatalogVersion, session.catalog_version_id)
    return _to_result_out(session, assessment, catalog)
