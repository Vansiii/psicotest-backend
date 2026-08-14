"""Siembra un cuestionario vocacional SINTÉTICO (D-14).

Ítems y dominios de redacción original, no derivados de un instrumento
psicométrico real. Los pesos por programa son ilustrativos y no provienen de
evidencia: solo permiten ejercitar el motor de afinidades del prototipo.

Uso: python -m app.assessment.seed
"""

from __future__ import annotations

import datetime as dt

from sqlalchemy import select

from app.assessment.models import AssessmentVersion, Domain, ProgramDomainWeight, Question
from app.core.db import Base, Session, engine

LABEL = "sintetico-2026-01"
SOURCE = "DATOS SINTÉTICOS DE PROTOTIPO — cuestionario no validado, no es un instrumento psicométrico"

DOMAINS = [
    ("analisis", "Análisis e investigación"),
    ("ayuda", "Ayuda y enseñanza"),
    ("organizacion", "Organización y gestión"),
    ("creacion", "Creación y comunicación"),
    ("tecnica", "Técnica y construcción"),
]

# (domain_code, texto del ítem) — Likert 1 (nada de acuerdo) a 5 (totalmente de acuerdo)
QUESTIONS = [
    ("analisis", "Disfruto resolver problemas que requieren analizar datos o información."),
    ("analisis", "Me interesa investigar por qué ocurren las cosas."),
    ("analisis", "Prefiero tareas que requieren pensar de forma lógica y sistemática."),
    ("analisis", "Me gusta comparar opciones con evidencia antes de decidir."),
    ("ayuda", "Disfruto explicarle algo a otra persona hasta que lo entiende."),
    ("ayuda", "Me interesa apoyar a alguien que está pasando un momento difícil."),
    ("ayuda", "Prefiero actividades donde colaboro directamente con otras personas."),
    ("ayuda", "Me gusta escuchar los problemas de otros y ayudar a pensar soluciones."),
    ("organizacion", "Disfruto planificar los pasos de una actividad o proyecto."),
    ("organizacion", "Me interesa coordinar el trabajo de un grupo de personas."),
    ("organizacion", "Prefiero tener reglas y procedimientos claros para trabajar."),
    ("organizacion", "Me gusta administrar tiempo, recursos o presupuestos."),
    ("creacion", "Disfruto crear contenido original, como textos, imágenes o diseños."),
    ("creacion", "Me interesa expresar ideas de forma creativa."),
    ("creacion", "Prefiero actividades donde puedo proponer algo nuevo."),
    ("creacion", "Me gusta comunicar una idea de manera clara y atractiva."),
    ("tecnica", "Disfruto construir, reparar o ensamblar cosas con las manos."),
    ("tecnica", "Me interesa entender cómo funcionan las máquinas o los sistemas."),
    ("tecnica", "Prefiero actividades prácticas en un taller o laboratorio."),
    ("tecnica", "Me gusta experimentar y probar cómo reaccionan los materiales."),
]

# external_id (de app.catalog.seed) -> {domain_code: peso}. Ilustrativo y
# sintético, desacoplado del catálogo: no hay FK ni dependencia de orden de
# siembra entre este módulo y app.catalog.seed.
PROGRAM_WEIGHTS: dict[str, dict[str, float]] = {
    "SYN-001": {"analisis": 0.9, "tecnica": 0.7, "organizacion": 0.5, "creacion": 0.3, "ayuda": 0.2},
    "SYN-002": {"tecnica": 0.9, "analisis": 0.8, "organizacion": 0.4, "creacion": 0.2, "ayuda": 0.2},
    "SYN-003": {"analisis": 0.95, "tecnica": 0.5, "organizacion": 0.4, "creacion": 0.2, "ayuda": 0.2},
    "SYN-004": {"organizacion": 0.9, "ayuda": 0.5, "analisis": 0.4, "creacion": 0.4, "tecnica": 0.2},
    "SYN-005": {"organizacion": 0.85, "analisis": 0.6, "tecnica": 0.3, "creacion": 0.2, "ayuda": 0.3},
    "SYN-006": {"analisis": 0.85, "organizacion": 0.6, "creacion": 0.3, "ayuda": 0.3, "tecnica": 0.2},
    "SYN-007": {"ayuda": 0.95, "creacion": 0.4, "organizacion": 0.4, "analisis": 0.4, "tecnica": 0.2},
    "SYN-008": {"creacion": 0.95, "ayuda": 0.5, "organizacion": 0.4, "analisis": 0.3, "tecnica": 0.2},
    "SYN-009": {"analisis": 0.95, "tecnica": 0.5, "organizacion": 0.5, "creacion": 0.2, "ayuda": 0.2},
}


def seed() -> str:
    Base.metadata.create_all(engine)
    with Session() as db:
        if db.scalars(select(AssessmentVersion).where(AssessmentVersion.label == LABEL)).first():
            return f"La versión '{LABEL}' ya existe; no se reescribe."

        version = AssessmentVersion(
            label=LABEL, source=SOURCE, is_synthetic=True, status="publicada", effective_from=dt.date(2026, 1, 1)
        )
        db.add(version)

        domains = {
            code: db.scalars(select(Domain).where(Domain.code == code)).first() or Domain(code=code, name=name)
            for code, name in DOMAINS
        }
        db.add_all(d for d in domains.values() if d.id is None)
        db.flush()

        for code, text in QUESTIONS:
            db.add(Question(assessment_version=version, domain=domains[code], text=text))

        for external_id, weights in PROGRAM_WEIGHTS.items():
            for code, weight in weights.items():
                db.add(ProgramDomainWeight(external_id=external_id, domain=domains[code], weight=weight))

        db.commit()
        return (
            f"Sembrada la versión '{LABEL}' con {len(QUESTIONS)} preguntas y "
            f"{len(PROGRAM_WEIGHTS)} programas ponderados."
        )


if __name__ == "__main__":
    print(seed())
