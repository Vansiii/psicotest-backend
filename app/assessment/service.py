"""Lógica de puntuación y afinidades, separada del transporte HTTP.

Fórmula de afinidad: promedio ponderado del puntaje normalizado por dominio,
usando los pesos sintéticos de `ProgramDomainWeight`.
ponytail: heurística ilustrativa, no una fórmula validada — reemplazar
cuando exista evidencia psicométrica real (docs/01 §5-6).
"""

from __future__ import annotations

from collections import defaultdict

from sqlalchemy import select
from sqlalchemy.orm import Session as OrmSession

from app.assessment.models import AssessmentVersion, ProgramDomainWeight, Question
from app.catalog.models import Program
from app.catalog.service import to_program_out
from app.core.versioning import resolve_published

LIMITATIONS_TEXT = (
    "Resultado de un prototipo de investigación con preguntas y perfiles sintéticos. "
    "No es un instrumento psicométrico validado ni un diagnóstico; no determina admisión, "
    "elegibilidad, éxito académico ni empleabilidad. Úsalo solo para explorar y conversar, "
    "no como una decisión."
)

EXPLORATION_PROMPTS = [
    "¿Qué actividades de estos programas te gustaría investigar más a fondo?",
    "¿Qué preguntas te gustaría resolver antes de decidir qué programas explorar?",
    "¿Qué información adicional necesitas verificar en la fuente oficial de cada programa?",
]

UNCERTAINTY_NOTE = (
    "Estimación exploratoria de un prototipo con datos sintéticos; no mide precisión "
    "psicométrica real."
)


def resolve_assessment_version(db: OrmSession, label: str | None) -> AssessmentVersion:
    return resolve_published(db, AssessmentVersion, label, "cuestionario")


def score_domains(questions: list[Question], responses_by_question_id: dict[int, int]) -> list[dict]:
    values_by_domain: dict[int, list[int]] = defaultdict(list)
    domain_by_id = {}
    for q in questions:
        values_by_domain[q.domain_id].append(responses_by_question_id[q.id])
        domain_by_id[q.domain_id] = q.domain

    scores = []
    for domain_id, values in values_by_domain.items():
        raw_average = sum(values) / len(values)
        domain = domain_by_id[domain_id]
        scores.append(
            {
                "domain_code": domain.code,
                "domain_name": domain.name,
                "raw_average": raw_average,
                "normalized": (raw_average - 1) / 4,
            }
        )
    return scores


def compute_affinities(db: OrmSession, domain_scores: list[dict], programs: list[Program]) -> list[dict]:
    normalized_by_code = {d["domain_code"]: d["normalized"] for d in domain_scores}
    external_ids = [p.external_id for p in programs]
    if not external_ids:
        return []

    weights = list(
        db.scalars(select(ProgramDomainWeight).where(ProgramDomainWeight.external_id.in_(external_ids)))
    )
    weights_by_program: dict[str, list[ProgramDomainWeight]] = defaultdict(list)
    for w in weights:
        weights_by_program[w.external_id].append(w)

    scored = []
    for program in programs:
        rows = weights_by_program.get(program.external_id)
        weight_sum = sum(r.weight for r in rows) if rows else 0
        if not rows or weight_sum == 0:
            # Sin pesos declarados: no se inventa una afinidad sin evidencia.
            continue

        affinity_score = sum(r.weight * normalized_by_code.get(r.domain.code, 0.0) for r in rows) / weight_sum
        top_domains = sorted(rows, key=lambda r: r.weight, reverse=True)[:2]
        reasons = [f"Coincide con tu interés en «{r.domain.name}»." for r in top_domains]

        scored.append(
            {
                "program": to_program_out(program).model_dump(mode="json"),
                "affinity_score": round(affinity_score, 4),
                "reasons": reasons,
            }
        )

    scored.sort(key=lambda s: s["affinity_score"], reverse=True)

    ranked = []
    last_rounded_score: float | None = None
    position = 0
    for s in scored:
        rounded = round(s["affinity_score"], 2)
        if rounded != last_rounded_score:
            position += 1
            last_rounded_score = rounded
        ranked.append({**s, "relative_position": position, "uncertainty": UNCERTAINTY_NOTE})
    return ranked
