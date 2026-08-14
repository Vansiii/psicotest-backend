"""Resolución compartida de "versión publicada o por label", usada por
cualquier dominio versionado (catálogo hoy; evaluación también)."""

from __future__ import annotations

from typing import TypeVar

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session as OrmSession

ModelT = TypeVar("ModelT")


def resolve_published(db: OrmSession, model: type[ModelT], label: str | None, noun: str) -> ModelT:
    """Sin `label` se sirve la última versión publicada. Una versión en
    borrador solo se alcanza pidiéndola por nombre."""
    stmt = select(model)
    if label:
        stmt = stmt.where(model.label == label)
    else:
        stmt = stmt.where(model.status == "publicada")
    version = db.scalars(stmt.order_by(model.created_at.desc())).first()
    if version is None:
        raise HTTPException(
            404,
            f"No existe la versión de {noun} '{label}'." if label else f"No hay ninguna versión de {noun} publicada.",
        )
    return version
