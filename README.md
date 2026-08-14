# psicotest-backend

Prototipo de investigación (decisiones D-13 y D-14, ver
`openspec/changes/f1-investigacion-institucional-seguridad/registros/decisiones.md`).
Expone un catálogo institucional **versionado y de solo lectura**, y un
cuestionario vocacional con motor de afinidades. Todos los datos sembrados
son sintéticos (`is_synthetic: true`) — no son la oferta real de la UAGRM ni
un instrumento psicométrico validado; esa reconciliación y esa validación
siguen pendientes (docs/03, decisión D-08; docs/01, docs/02).

Fuera de alcance: aprobación institucional, consentimiento/asentimiento
formal, canal de derivación real a Orientación Vocacional. Ver `docs/` y
`openspec/` para el contexto completo de investigación.

## Estructura

```text
app/
├── main.py         # composición: crea la app FastAPI, monta routers
├── core/           # infraestructura compartida (db, resolución de versiones)
├── catalog/        # dominio de catálogo: models, schemas, service, router, seed
└── assessment/     # dominio de evaluación: cuestionario, sesiones, afinidades
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

**Trabaja siempre dentro del entorno virtual.** Instalar este proyecto al Python
del sistema hace que `import app` resuelva desde cualquier carpeta, lo que
enmascara imports mal puestos que en CI sí fallarían.

```bash
python -m venv .venv                      # una sola vez
source .venv/Scripts/activate             # Windows (Git Bash); Linux/macOS: .venv/bin/activate
python -m pip install -e ".[dev]"

python -m app.catalog.seed                # siembra el catálogo sintético si no existe
python -m app.assessment.seed             # siembra el cuestionario sintético si no existe
python -m pytest -q                       # pruebas sobre SQLite en memoria
python -m uvicorn app.main:app --reload   # http://127.0.0.1:8000/docs
```

`.venv/` está en `.gitignore`. Para comprobar que estás dentro:

```bash
python -c "import sys; print(sys.prefix != sys.base_prefix)"   # debe imprimir True
```

En CI no se crea venv: el runner de GitHub Actions es un contenedor desechable,
así que instalar al Python del contenedor es correcto y está aislado por sí solo.
