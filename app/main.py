"""API de catálogo de TestPsico — solo lectura.

Fuera de alcance por decisión de investigación (docs/06): puntuación,
afinidades, recomendaciones, sesiones y respuestas. Este servicio expone la
oferta versionada y nada más.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as OrmSession

from app.models import Campus, CatalogVersion, Faculty, Program, Session
from app.schemas import CatalogRef, ProfileOut, ProgramDetail, ProgramList, ProgramOut

app = FastAPI(
    title="TestPsico — catálogo institucional",
    version="0.1.0",
    description=(
        "Prototipo de investigación. La oferta servida puede ser sintética: "
        "cada respuesta declara su procedencia en `catalog`. No expresa "
        "admisión, elegibilidad ni recomendación."
    ),
)


def get_session():
    with Session() as session:
        yield session


Db = Annotated[OrmSession, Depends(get_session)]


def _resolve_version(db: OrmSession, label: str | None) -> CatalogVersion:
    """Sin `label` se sirve la última versión publicada. Una versión en
    borrador solo se alcanza pidiéndola por nombre."""
    stmt = select(CatalogVersion)
    if label:
        stmt = stmt.where(CatalogVersion.label == label)
    else:
        stmt = stmt.where(CatalogVersion.status == "publicada")
    version = db.scalars(stmt.order_by(CatalogVersion.created_at.desc())).first()
    if version is None:
        raise HTTPException(
            404,
            f"No existe la versión de catálogo '{label}'."
            if label
            else "No hay ninguna versión de catálogo publicada.",
        )
    return version


def _to_out(program: Program) -> ProgramOut:
    return ProgramOut(
        external_id=program.external_id,
        name=program.name,
        faculty=program.faculty.name,
        campus=program.campus.name,
        level=program.level,
        modality=program.modality,
        availability=program.availability,
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/catalog/versions", response_model=list[CatalogRef])
def list_versions(db: Db) -> list[CatalogVersion]:
    return list(db.scalars(select(CatalogVersion).order_by(CatalogVersion.created_at.desc())))


@app.get("/programs", response_model=ProgramList)
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
    version = _resolve_version(db, catalog)
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
        programs=[_to_out(p) for p in programs],
    )


@app.get("/programs/{external_id}", response_model=ProgramDetail)
def get_program(
    external_id: str,
    db: Db,
    catalog: Annotated[str | None, Query(description="Etiqueta de versión")] = None,
) -> ProgramDetail:
    version = _resolve_version(db, catalog)
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
        **_to_out(program).model_dump(),
        catalog=CatalogRef.model_validate(version),
        profile=ProfileOut.model_validate(program.profiles[0]) if program.profiles else None,
    )
