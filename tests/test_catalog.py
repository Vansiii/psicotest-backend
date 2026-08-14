"""Comprobación de la API de catálogo sobre SQLite en memoria."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.catalog import seed as seed_module
from app.catalog.models import CatalogVersion
from app.core.db import Base, get_session
from app.main import app


@pytest.fixture(name="client")
def client_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Session = sessionmaker(engine, expire_on_commit=False)
    Base.metadata.create_all(engine)

    # El seed escribe con su propio engine/Session; se apuntan al de prueba.
    seed_module.engine = engine
    seed_module.Session = Session
    seed_module.seed()

    app.dependency_overrides[get_session] = lambda: (yield from _session(Session))
    yield TestClient(app)
    app.dependency_overrides.clear()


def _session(Session):
    with Session() as s:
        yield s


def test_lista_completa_sin_prefiltro(client):
    body = client.get("/programs").json()
    assert body["count"] == len(seed_module.PROGRAMS)
    assert body["catalog"]["label"] == seed_module.LABEL


def test_toda_respuesta_declara_procedencia_sintetica(client):
    for url in ("/programs", "/programs/SYN-001"):
        assert client.get(url).json()["catalog"]["is_synthetic"] is True


def test_filtros_explicitos_se_combinan(client):
    fcet = client.get("/programs", params={"faculty": "FCET"}).json()
    assert fcet["count"] == 3
    assert fcet["programs"][0]["faculty_code"] == "FCET"

    combinado = client.get(
        "/programs", params={"faculty": "FCET", "modality": "presencial"}
    ).json()
    assert {p["external_id"] for p in combinado["programs"]} == {"SYN-001", "SYN-002"}

    assert client.get("/programs", params={"faculty": "NO-EXISTE"}).json()["count"] == 0


def test_detalle_incluye_perfil_con_limites(client):
    body = client.get("/programs/SYN-007").json()
    assert body["faculty"] == "Facultad de Humanidades"
    assert body["profile"]["activities"]
    assert "no expresa requisito de admisión" in body["profile"]["limitations"].lower()


def test_programa_inexistente_es_404(client):
    assert client.get("/programs/SYN-999").status_code == 404


def test_sin_version_publicada_responde_404(client):
    with seed_module.Session() as db:
        db.query(CatalogVersion).update({"status": "borrador"})
        db.commit()
    respuesta = client.get("/programs")
    assert respuesta.status_code == 404
    assert "publicada" in respuesta.json()["detail"]


def test_borrador_solo_accesible_por_nombre(client):
    with seed_module.Session() as db:
        db.query(CatalogVersion).update({"status": "borrador"})
        db.commit()
    assert client.get("/programs", params={"catalog": seed_module.LABEL}).status_code == 200


def test_seed_no_reescribe_una_version_existente(client):
    assert "ya existe" in seed_module.seed()


def test_nueva_version_no_altera_la_anterior(client):
    """Principio de inmutabilidad (docs/05 §6): publicar una segunda
    instantánea no debe cambiar ni un solo campo de la primera."""
    v1_antes = client.get("/programs", params={"catalog": seed_module.LABEL}).json()

    seed_module.seed_v2()

    v1_despues = client.get("/programs", params={"catalog": seed_module.LABEL}).json()
    assert v1_despues == v1_antes

    v2 = client.get("/programs", params={"catalog": seed_module.LABEL_V2}).json()
    assert v2["count"] == len(seed_module.PROGRAMS_V2)


def test_sin_catalog_param_resuelve_a_la_version_publicada_mas_reciente(client):
    seed_module.seed_v2()
    body = client.get("/programs").json()
    assert body["catalog"]["label"] == seed_module.LABEL_V2


def test_catalog_versions_lista_ambas_sin_perder_la_primera(client):
    seed_module.seed_v2()
    labels = {v["label"] for v in client.get("/catalog/versions").json()}
    assert labels == {seed_module.LABEL, seed_module.LABEL_V2}
