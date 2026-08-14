"""Rutas HTTP del dominio de catálogo — solo lectura.

Fuera de alcance por decisión de investigación (docs/06): puntuación,
afinidades, recomendaciones, sesiones y respuestas. Este router expone la
oferta versionada y nada más.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as OrmSession

from app.catalog.models import Campus, CatalogVersion, Faculty, Program
from app.catalog.schemas import CatalogRef, ProfileOut, ProgramDetail, ProgramList
from app.catalog.service import resolve_version, to_program_out
from app.core.db import get_session

router = APIRouter(tags=["catalog"])

Db = Annotated[OrmSession, Depends(get_session)]


@router.get("/catalog/versions", response_model=list[CatalogRef])
def list_versions(db: Db) -> list[CatalogVersion]:
    return list(db.scalars(select(CatalogVersion).order_by(CatalogVersion.created_at.desc())))


@router.get("/programs", response_model=ProgramList)
def list_programs(
    db: Db,
    catalog: Annotated[str | None, Query(description="Etiqueta de versión")] = None,
    faculty: Annotated[str | None, Query(description="Código de facultad")] = None,
    campus: Annotated[str | None, Query(description="Código de campus o sitio")] = None,
    level: str | None = None,
    modality: str | None = None,
) -> ProgramList:
    """Facultad, campus, nivel y modalidad son filtros explícitos y opcionales.
    Sin ellos se devuelve toda la oferta de la versión: docs/02 prohíbe un
    pre-filtro obligatorio por facultad."""
    version = resolve_version(db, catalog)
    stmt = select(Program).where(Program.catalog_version_id == version.id)
    if faculty:
        stmt = stmt.join(Program.faculty).where(Faculty.code == faculty)
    if campus:
        stmt = stmt.join(Program.campus).where(Campus.code == campus)
    if level:
        stmt = stmt.where(Program.level == level)
    if modality:
        stmt = stmt.where(Program.modality == modality)

    programs = list(db.scalars(stmt.order_by(Program.name)))
    return ProgramList(
        catalog=CatalogRef.model_validate(version),
        count=len(programs),
        programs=[to_program_out(p) for p in programs],
    )


@router.get("/programs/{external_id}", response_model=ProgramDetail)
def get_program(
    external_id: str,
    db: Db,
    catalog: Annotated[str | None, Query(description="Etiqueta de versión")] = None,
) -> ProgramDetail:
    version = resolve_version(db, catalog)
    program = db.scalars(
        select(Program).where(
            Program.catalog_version_id == version.id,
            Program.external_id == external_id,
        )
    ).first()
    if program is None:
        raise HTTPException(
            404, f"El programa '{external_id}' no existe en la versión '{version.label}'."
        )
    return ProgramDetail(
        **to_program_out(program).model_dump(),
        catalog=CatalogRef.model_validate(version),
        profile=ProfileOut.model_validate(program.profiles[0]) if program.profiles else None,
    )
