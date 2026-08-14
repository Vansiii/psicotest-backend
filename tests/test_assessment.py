"""Comprobación de la API de evaluación sobre SQLite en memoria."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.assessment import seed as assessment_seed_module
from app.catalog import seed as catalog_seed_module
from app.core.db import Base, get_session
from app.main import app


@pytest.fixture(name="client")
def client_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Session = sessionmaker(engine, expire_on_commit=False)
    Base.metadata.create_all(engine)

    catalog_seed_module.engine = engine
    catalog_seed_module.Session = Session
    catalog_seed_module.seed()

    assessment_seed_module.engine = engine
    assessment_seed_module.Session = Session
    assessment_seed_module.seed()

    app.dependency_overrides[get_session] = lambda: (yield from _session(Session))
    yield TestClient(app)
    app.dependency_overrides.clear()


def _session(Session):
    with Session() as s:
        yield s


def test_preguntas_cubren_los_cinco_dominios(client):
    body = client.get("/assessment/questions").json()
    assert len(body["questions"]) == len(assessment_seed_module.QUESTIONS)
    assert {q["domain_code"] for q in body["questions"]} == {code for code, _ in assessment_seed_module.DOMAINS}


def _all_responses(client, value_by_domain: dict[str, int] | None = None, default: int = 3) -> list[dict]:
    questions = client.get("/assessment/questions").json()["questions"]
    values = value_by_domain or {}
    return [
        {"question_id": q["id"], "value": values.get(q["domain_code"], default)}
        for q in questions
    ]


def test_envio_completo_calcula_puntajes_y_afinidades(client):
    responses = _all_responses(client, default=3)
    body = client.post("/assessment/sessions", json={"responses": responses}).json()

    assert len(body["domain_scores"]) == 5
    for domain_score in body["domain_scores"]:
        assert domain_score["raw_average"] == 3
        assert domain_score["normalized"] == pytest.approx(0.5)

    scores = [a["affinity_score"] for a in body["affinities"]]
    assert scores == sorted(scores, reverse=True)
    # Solo la v1 del catálogo está sembrada en este fixture (SYN-001..008);
    # SYN-009 (v2) no aparece aunque tenga pesos declarados.
    assert len(body["affinities"]) == len(catalog_seed_module.PROGRAMS)


def test_afinidad_favorece_el_dominio_mejor_respondido(client):
    responses = _all_responses(client, value_by_domain={"analisis": 5}, default=1)
    body = client.post("/assessment/sessions", json={"responses": responses}).json()

    primero = body["affinities"][0]
    assert primero["relative_position"] == 1
    assert primero["program"]["external_id"] == "SYN-003"  # mayor peso sintético en "analisis"


def test_respuestas_incompletas_son_400(client):
    responses = _all_responses(client)[:-1]
    resp = client.post("/assessment/sessions", json={"responses": responses})
    assert resp.status_code == 400


def test_pregunta_desconocida_es_400(client):
    responses = _all_responses(client)
    responses[0]["question_id"] = 999999
    resp = client.post("/assessment/sessions", json={"responses": responses})
    assert resp.status_code == 400


def test_valor_fuera_de_rango_es_422(client):
    responses = _all_responses(client)
    responses[0]["value"] = 6
    resp = client.post("/assessment/sessions", json={"responses": responses})
    assert resp.status_code == 422


def test_sesion_es_recuperable_y_estable(client):
    responses = _all_responses(client)
    creado = client.post("/assessment/sessions", json={"responses": responses}).json()

    recuperado = client.get(f"/assessment/sessions/{creado['session_id']}").json()
    assert recuperado == creado


def test_sesion_inexistente_es_404(client):
    assert client.get("/assessment/sessions/no-existe").status_code == 404
