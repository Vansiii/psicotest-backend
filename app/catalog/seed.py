"""Siembra una versión de catálogo SINTÉTICA.

Estos programas NO provienen de una fuente autorizada de la UAGRM. La
discrepancia real está sin resolver: admisiones informa 18 facultades y 69
programas [S29] y la página de carreras expone ~80 entradas con repeticiones
[S30]. Elegir una de esas cifras aquí sería inventar catálogo, así que se
siembra una muestra reducida y marcada, suficiente para ejercitar la API.

Uso: python -m app.catalog.seed
"""

from __future__ import annotations

import datetime as dt

from sqlalchemy import select

from app.catalog.models import Campus, CatalogVersion, Faculty, Program, ProgramProfile
from app.core.db import Base, Session, engine

LABEL = "sintetico-2026-01"
SOURCE = "DATOS SINTÉTICOS DE PROTOTIPO — no provienen de una fuente autorizada UAGRM"

FACULTIES = [
    ("FCET", "Facultad de Ciencias Exactas y Tecnología"),
    ("FCEE", "Facultad de Ciencias Económicas y Empresariales"),
    ("FH", "Facultad de Humanidades"),
]

CAMPUSES = [
    ("SC-CENTRAL", "Campus central"),
    ("SC-NORTE", "Sitio norte"),
]

# (external_id, nombre, facultad, campus, nivel, modalidad, disponibilidad, resumen, actividades)
PROGRAMS = [
    (
        "SYN-001", "Programa sintético de análisis de sistemas", "FCET", "SC-CENTRAL",
        "licenciatura", "presencial", "oferta_regular",
        "Programa de ejemplo orientado al diseño y evaluación de sistemas de información.",
        ["modelar procesos", "programar y probar software", "documentar requisitos"],
    ),
    (
        "SYN-002", "Programa sintético de ingeniería de materiales", "FCET", "SC-NORTE",
        "licenciatura", "presencial", "oferta_regular",
        "Programa de ejemplo centrado en propiedades y ensayo de materiales.",
        ["realizar ensayos de laboratorio", "interpretar mediciones", "redactar informes técnicos"],
    ),
    (
        "SYN-003", "Programa sintético de matemática aplicada", "FCET", "SC-CENTRAL",
        "licenciatura", "semipresencial", "cupo_limitado",
        "Programa de ejemplo con énfasis en modelado cuantitativo.",
        ["formular modelos", "demostrar resultados", "analizar datos"],
    ),
    (
        "SYN-004", "Programa sintético de administración", "FCEE", "SC-CENTRAL",
        "licenciatura", "presencial", "oferta_regular",
        "Programa de ejemplo sobre organización y gestión de recursos.",
        ["planificar operaciones", "coordinar equipos", "evaluar presupuestos"],
    ),
    (
        "SYN-005", "Programa sintético de contaduría", "FCEE", "SC-NORTE",
        "licenciatura", "a_distancia", "oferta_regular",
        "Programa de ejemplo sobre registro y control financiero.",
        ["registrar operaciones", "conciliar cuentas", "preparar estados financieros"],
    ),
    (
        "SYN-006", "Programa sintético de economía", "FCEE", "SC-CENTRAL",
        "licenciatura", "presencial", "sin_informacion",
        "Programa de ejemplo sobre análisis de mercados y política económica.",
        ["analizar series económicas", "comparar políticas", "elaborar informes"],
    ),
    (
        "SYN-007", "Programa sintético de psicología educativa", "FH", "SC-CENTRAL",
        "licenciatura", "presencial", "oferta_regular",
        "Programa de ejemplo sobre procesos de aprendizaje en contextos educativos.",
        ["observar procesos de aprendizaje", "diseñar intervenciones", "entrevistar"],
    ),
    (
        "SYN-008", "Programa sintético de comunicación", "FH", "SC-NORTE",
        "licenciatura", "semipresencial", "cupo_limitado",
        "Programa de ejemplo sobre producción y análisis de mensajes.",
        ["producir contenidos", "analizar audiencias", "editar piezas"],
    ),
]

LIMITATION = (
    "Perfil sintético de prototipo. Describe el programa, no a una persona ideal. "
    "No expresa requisito de admisión, elegibilidad ni pronóstico de éxito."
)

LABEL_V2 = "sintetico-2026-02"

# v2 demuestra que una nueva instantánea no reescribe la anterior (docs/05 §6):
# reutiliza los mismos programas y agrega uno nuevo, sin tocar los datos de v1.
PROGRAMS_V2 = PROGRAMS + [
    (
        "SYN-009", "Programa sintético de estadística", "FCET", "SC-CENTRAL",
        "licenciatura", "presencial", "oferta_regular",
        "Programa de ejemplo agregado en la segunda instantánea del catálogo.",
        ["diseñar muestreos", "analizar variabilidad", "comunicar resultados"],
    ),
]


def _seed_version(label: str, status: str, effective_from: dt.date, programs: list[tuple]) -> str:
    """Crea una instantánea de catálogo si `label` no existe. No modifica
    ninguna instantánea previa: cada llamada agrega filas nuevas."""
    Base.metadata.create_all(engine)
    with Session() as db:
        if db.scalars(select(CatalogVersion).where(CatalogVersion.label == label)).first():
            return f"La versión '{label}' ya existe; no se reescribe."

        version = CatalogVersion(
            label=label, source=SOURCE, is_synthetic=True, status=status, effective_from=effective_from
        )
        db.add(version)

        faculties = {
            code: db.scalars(select(Faculty).where(Faculty.code == code)).first() or Faculty(code=code, name=name)
            for code, name in FACULTIES
        }
        campuses = {
            code: db.scalars(select(Campus).where(Campus.code == code)).first() or Campus(code=code, name=name)
            for code, name in CAMPUSES
        }
        db.add_all(f for f in faculties.values() if f.id is None)
        db.add_all(c for c in campuses.values() if c.id is None)
        db.flush()

        for ext_id, name, fac, camp, level, modality, avail, summary, activities in programs:
            program = Program(
                catalog_version=version,
                external_id=ext_id,
                name=name,
                faculty_id=faculties[fac].id,
                campus_id=campuses[camp].id,
                level=level,
                modality=modality,
                availability=avail,
            )
            db.add(program)
            db.flush()
            db.add(
                ProgramProfile(
                    program_id=program.id,
                    version=1,
                    summary=summary,
                    activities=activities,
                    sources=[SOURCE],
                    limitations=LIMITATION,
                    reviewed_at=effective_from,
                )
            )

        db.commit()
        return f"Sembrada la versión '{label}' con {len(programs)} programas sintéticos."


def seed() -> str:
    return _seed_version(LABEL, "publicada", dt.date(2026, 1, 1), PROGRAMS)


def seed_v2() -> str:
    return _seed_version(LABEL_V2, "publicada", dt.date(2026, 2, 1), PROGRAMS_V2)


if __name__ == "__main__":
    print(seed())
    print(seed_v2())
