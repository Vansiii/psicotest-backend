"""Infraestructura de base de datos, compartida por cualquier dominio futuro
(catálogo hoy; evaluación, puntuación, afinidades más adelante).

No pertenece a ningún dominio: define cómo se conecta, no qué se guarda.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import NullPool


class Base(DeclarativeBase):
    pass


def database_url() -> str:
    load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")
    raw = os.getenv("CONNECTION_STRING")
    if not raw:
        return "sqlite:///./catalogo.db"
    return raw.replace("postgresql://", "postgresql+psycopg://", 1)


# NullPool: el pooler transaccional de Supabase (puerto 6543) ya agrupa
# conexiones; un segundo pool encima agota el límite del proyecto.
engine = create_engine(database_url(), poolclass=NullPool)
Session = sessionmaker(engine, expire_on_commit=False)


def get_session():
    with Session() as session:
        yield session
