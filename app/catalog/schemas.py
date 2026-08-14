"""Contrato de lectura del catálogo. El backend es dueño de estas formas
(docs/05 §7); el frontend las consume y no las redefine."""

from __future__ import annotations

import datetime as dt

from pydantic import BaseModel, ConfigDict


class CatalogRef(BaseModel):
    """Procedencia que acompaña a toda respuesta: sin ella el consumidor no
    puede saber si está viendo datos autorizados o de prototipo."""

    model_config = ConfigDict(from_attributes=True)

    label: str
    source: str
    is_synthetic: bool
    status: str
    effective_from: dt.date | None


class ProgramOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    external_id: str
    name: str
    faculty: str
    faculty_code: str
    campus: str
    campus_code: str
    level: str
    modality: str
    availability: str


class ProfileOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    version: int
    summary: str
    activities: list[str]
    sources: list[str]
    limitations: str
    reviewed_at: dt.date | None


class ProgramDetail(ProgramOut):
    catalog: CatalogRef
    profile: ProfileOut | None


class ProgramList(BaseModel):
    catalog: CatalogRef
    count: int
    programs: list[ProgramOut]
