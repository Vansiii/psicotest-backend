"""Lógica de consulta del catálogo, separada del transporte HTTP.

`router.py` traduce peticiones/respuestas; este módulo decide qué versión
resolver y cómo proyectar una fila `Program` al contrato de salida.
"""

from __future__ import annotations

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session as OrmSession

from app.catalog.models import CatalogVersion, Program
from app.catalog.schemas import ProgramOut


def resolve_version(db: OrmSession, label: str | None) -> CatalogVersion:
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


def to_program_out(program: Program) -> ProgramOut:
    # faculty_code/campus_code se exponen porque son los valores que aceptan
    # los filtros de esta misma API: sin ellos el consumidor no puede
    # construir una consulta filtrada válida a partir de una respuesta previa.
    return ProgramOut(
        external_id=program.external_id,
        name=program.name,
        faculty=program.faculty.name,
        faculty_code=program.faculty.code,
        campus=program.campus.name,
        campus_code=program.campus.code,
        level=program.level,
        modality=program.modality,
        availability=program.availability,
    )
