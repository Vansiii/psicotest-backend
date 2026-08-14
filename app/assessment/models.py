"""Entidades del dominio de evaluación — cuestionario vocacional, respuestas
y afinidades. Prototipo con contenido sintético (D-14): no es un instrumento
psicométrico validado. Ver docs/01 y docs/02 para los límites de fondo.

Regla de inmutabilidad, igual que en `catalog` (docs/05 §6): `TestSession`
congela `domain_scores` y `affinities` al momento de calcularlos — un cambio
posterior en el catálogo o el cuestionario no debe reescribir un resultado
ya emitido.
"""

from __future__ import annotations

import datetime as dt
import uuid

from sqlalchemy import JSON, Boolean, Date, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.catalog import models as _catalog_models  # noqa: F401  # registra catalog_version en Base.metadata
from app.core.db import Base


class AssessmentVersion(Base):
    """Instantánea del cuestionario, igual patrón que `CatalogVersion`."""

    __tablename__ = "assessment_version"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(64), unique=True)
    source: Mapped[str] = mapped_column(String(512))
    is_synthetic: Mapped[bool] = mapped_column(Boolean, default=True)
    status: Mapped[str] = mapped_column(String(16), default="borrador")  # borrador | publicada
    effective_from: Mapped[dt.date | None] = mapped_column(Date, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)

    questions: Mapped[list["Question"]] = relationship(back_populates="assessment_version")


class Domain(Base):
    """Dominio de interés vocacional. Vocabulario original del prototipo, no
    copiado de un instrumento existente."""

    __tablename__ = "domain"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(32), unique=True)
    name: Mapped[str] = mapped_column(String(128))


class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    assessment_version_id: Mapped[int] = mapped_column(ForeignKey("assessment_version.id"))
    domain_id: Mapped[int] = mapped_column(ForeignKey("domain.id"))
    text: Mapped[str] = mapped_column(String(512))

    assessment_version: Mapped[AssessmentVersion] = relationship(back_populates="questions")
    domain: Mapped[Domain] = relationship()


class ProgramDomainWeight(Base):
    """Peso ilustrativo y sintético de un programa en un dominio de interés.

    Se referencia por `external_id` (identidad estable del programa, docs/02)
    y no por `Program.id`: el mismo programa reaparece con un `Program.id`
    distinto en cada `CatalogVersion`, y el peso no depende de la instantánea.
    """

    __tablename__ = "program_domain_weight"
    __table_args__ = (UniqueConstraint("external_id", "domain_id"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    external_id: Mapped[str] = mapped_column(String(64))
    domain_id: Mapped[int] = mapped_column(ForeignKey("domain.id"))
    weight: Mapped[float] = mapped_column(Float)

    domain: Mapped[Domain] = relationship()


class TestSession(Base):
    """Una ejecución completa del cuestionario. Nace ya cerrada: no hay
    estado "en progreso" en el backend (el cliente acumula respuestas y las
    envía juntas), así que el resultado es inmutable desde su creación."""

    __tablename__ = "test_session"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, default=lambda: uuid.uuid4().hex)
    assessment_version_id: Mapped[int] = mapped_column(ForeignKey("assessment_version.id"))
    catalog_version_id: Mapped[int] = mapped_column(ForeignKey("catalog_version.id"))
    submitted_at: Mapped[dt.datetime] = mapped_column(DateTime)
    domain_scores: Mapped[list] = mapped_column(JSON)
    affinities: Mapped[list] = mapped_column(JSON)


class Response(Base):
    """Respuesta cruda a una pregunta, conservada para trazabilidad/auditoría
    (docs/05 §9), separada del resultado calculado."""

    __tablename__ = "response"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[str] = mapped_column(ForeignKey("test_session.id"))
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    value: Mapped[int] = mapped_column(Integer)
