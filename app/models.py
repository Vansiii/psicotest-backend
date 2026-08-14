"""Modelo de catálogo institucional versionado.

Regla de inmutabilidad (docs/05 §6): un resultado histórico no se reescribe.
Se cumple sin triggers ni auditoría: la API es de solo lectura y una corrección
del catálogo se publica como una `CatalogVersion` nueva, nunca editando una
existente. `app/seed.py` es el único escritor.
"""

from __future__ import annotations

import datetime as dt
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import (
    JSON,
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    String,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy.pool import NullPool


class Base(DeclarativeBase):
    pass


class CatalogVersion(Base):
    """Instantánea autorizada de la oferta. `is_synthetic` es obligatorio y
    viaja en cada respuesta de la API: doc 04 exige distinguir un ejemplo
    sintético de una norma UAGRM."""

    __tablename__ = "catalog_version"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(64), unique=True)
    source: Mapped[str] = mapped_column(String(512))
    is_synthetic: Mapped[bool] = mapped_column(Boolean, default=True)
    status: Mapped[str] = mapped_column(String(16), default="borrador")  # borrador | publicada
    effective_from: Mapped[dt.date | None] = mapped_column(Date, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)

    programs: Mapped[list["Program"]] = relationship(back_populates="catalog_version")


class Faculty(Base):
    __tablename__ = "faculty"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(32), unique=True)
    name: Mapped[str] = mapped_column(String(256))


class Campus(Base):
    __tablename__ = "campus"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(32), unique=True)
    name: Mapped[str] = mapped_column(String(256))


class Program(Base):
    """Carrera o programa. `external_id` es el ID estable de la fuente; es único
    dentro de una versión, no globalmente: el mismo programa reaparece en cada
    versión publicada."""

    __tablename__ = "program"
    __table_args__ = (UniqueConstraint("catalog_version_id", "external_id"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    catalog_version_id: Mapped[int] = mapped_column(ForeignKey("catalog_version.id"))
    external_id: Mapped[str] = mapped_column(String(64))
    name: Mapped[str] = mapped_column(String(256))
    faculty_id: Mapped[int] = mapped_column(ForeignKey("faculty.id"))
    campus_id: Mapped[int] = mapped_column(ForeignKey("campus.id"))
    level: Mapped[str] = mapped_column(String(64))
    modality: Mapped[str] = mapped_column(String(64))
    availability: Mapped[str] = mapped_column(String(64))

    catalog_version: Mapped[CatalogVersion] = relationship(back_populates="programs")
    faculty: Mapped[Faculty] = relationship()
    campus: Mapped[Campus] = relationship()
    # Un perfil se revisa varias veces; `profiles[0]` es la revisión vigente.
    profiles: Mapped[list["ProgramProfile"]] = relationship(
        back_populates="program", order_by="ProgramProfile.version.desc()"
    )


class ProgramProfile(Base):
    """Perfil educativo del programa (docs/02): describe el programa y sus
    fuentes, nunca una persona ideal ni un requisito de admisión."""

    __tablename__ = "program_profile"
    __table_args__ = (UniqueConstraint("program_id", "version"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    program_id: Mapped[int] = mapped_column(ForeignKey("program.id"))
    version: Mapped[int] = mapped_column(default=1)
    summary: Mapped[str] = mapped_column(String(1024))
    activities: Mapped[list[str]] = mapped_column(JSON, default=list)
    sources: Mapped[list[str]] = mapped_column(JSON, default=list)
    limitations: Mapped[str] = mapped_column(String(1024))
    reviewed_at: Mapped[dt.date | None] = mapped_column(Date, nullable=True)

    program: Mapped[Program] = relationship(back_populates="profiles")


def database_url() -> str:
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    raw = os.getenv("CONNECTION_STRING")
    if not raw:
        return "sqlite:///./catalogo.db"
    return raw.replace("postgresql://", "postgresql+psycopg://", 1)


# NullPool: el pooler transaccional de Supabase (puerto 6543) ya agrupa
# conexiones; un segundo pool encima agota el límite del proyecto.
engine = create_engine(database_url(), poolclass=NullPool)
Session = sessionmaker(engine, expire_on_commit=False)
