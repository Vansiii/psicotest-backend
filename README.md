# psicotest-backend

Prototipo de investigación (decisión D-13, ver
`openspec/changes/f1-investigacion-institucional-seguridad/registros/decisiones.md`).
Expone un catálogo institucional **versionado y de solo lectura**. Los datos
sembrados son sintéticos (`is_synthetic: true`) — no son la oferta real de la
UAGRM; esa reconciliación sigue pendiente (docs/03, decisión D-08).

Fuera de alcance: evaluación, puntuación, afinidades, recomendaciones. Ver
`docs/` y `openspec/` para el contexto completo de investigación.

## Estructura

```text
app/
├── main.py       # composición: crea la app FastAPI, monta routers
├── core/         # infraestructura compartida (motor/sesión de base de datos)
└── catalog/      # dominio de catálogo: models, schemas, service, router, seed
```

Cada dominio futuro autorizado (evaluación, puntuación, afinidades) se
agregaría como un paquete hermano de `catalog/`, con su propio
`models.py`/`schemas.py`/`service.py`/`router.py` — no se crean vacíos por
adelantado.

## Requisitos

- Python 3.12+
- Opcional: `CONNECTION_STRING` en `.env` (Postgres). Sin ella, usa SQLite
  local (`./catalogo.db`).

## Uso

```bash
python -m pip install -e ".[dev]"
python -m app.catalog.seed   # siembra las versiones sintéticas si no existen
python -m pytest -q          # pruebas sobre SQLite en memoria
python -m uvicorn app.main:app --reload   # http://127.0.0.1:8000/docs
```
