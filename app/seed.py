"""Siembra una versión de catálogo SINTÉTICA.

Estos programas NO provienen de una fuente autorizada de la UAGRM. La
discrepancia real está sin resolver: admisiones informa 18 facultades y 69
programas [S29] y la página de carreras expone ~80 entradas con repeticiones
[S30]. Elegir una de esas cifras aquí sería inventar catálogo, así que se
siembra una muestra reducida y marcada, suficiente para ejercitar la API.

Uso: python -m app.seed
"""

from __future__ import annotations

import datetime as dt

from sqlalchemy import select

from app.models import Base, Campus, CatalogVersion, Faculty, Program, ProgramProfile, Session, engine

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


def seed() -> str:
    Base.metadata.create_all(engine)
    with Session() as db:
        if db.scalars(select(CatalogVersion).where(CatalogVersion.label == LABEL)).first():
            return f"La versión '{LABEL}' ya existe; no se reescribe."

        version = CatalogVersion(
            label=LABEL,
            source=SOURCE,
            is_synthetic=True,
            status="publicada",
            effective_from=dt.date(2026, 1, 1),
        )
        db.add(version)

        faculties = {code: Faculty(code=code, name=name) for code, name in FACULTIES}
        campuses = {code: Campus(code=code, name=name) for code, name in CAMPUSES}
        for existing in (faculties, campuses):
            db.add_all(existing.values())
        db.flush()

        for ext_id, name, fac, camp, level, modality, avail, summary, activities in PROGRAMS:
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
                    reviewed_at=dt.date(2026, 1, 1),
                )
            )

        db.commit()
        return f"Sembrada la versión '{LABEL}' con {len(PROGRAMS)} programas sintéticos."


if __name__ == "__main__":
    print(seed())
