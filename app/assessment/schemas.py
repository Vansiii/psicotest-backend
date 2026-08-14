"""Contrato de evaluación vocacional. Igual regla que en `catalog` (docs/05
§7): el backend es dueño de estas formas, el frontend las consume."""

from __future__ import annotations

import datetime as dt

from pydantic import BaseModel, ConfigDict, Field

from app.catalog.schemas import CatalogRef, ProgramOut


class AssessmentRef(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    label: str
    source: str
    is_synthetic: bool
    status: str
    effective_from: dt.date | None


class QuestionOut(BaseModel):
    id: int
    text: str
    domain_code: str


class QuestionList(BaseModel):
    assessment: AssessmentRef
    questions: list[QuestionOut]


class ResponseIn(BaseModel):
    question_id: int
    value: int = Field(ge=1, le=5)


class SessionCreate(BaseModel):
    assessment: str | None = None
    catalog: str | None = None
    responses: list[ResponseIn]


class DomainScoreOut(BaseModel):
    domain_code: str
    domain_name: str
    raw_average: float
    normalized: float


class AffinityOut(BaseModel):
    relative_position: int
    program: ProgramOut
    affinity_score: float
    reasons: list[str]
    uncertainty: str


class ResultOut(BaseModel):
    session_id: str
    assessment: AssessmentRef
    catalog: CatalogRef
    submitted_at: dt.datetime
    domain_scores: list[DomainScoreOut]
    affinities: list[AffinityOut]
    limitations: str
    exploration_prompts: list[str]
