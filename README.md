# psicotest-backend

Prototipo de investigación (decisión D-13, ver
`openspec/changes/f1-investigacion-institucional-seguridad/registros/decisiones.md`).
Expone un catálogo institucional **versionado y de solo lectura**. Los datos
sembrados son sintéticos (`is_synthetic: true`) — no son la oferta real de la
UAGRM; esa reconciliación sigue pendiente (docs/03, decisión D-08).

Fuera de alcance: evaluación, puntuación, afinidades, recomendaciones. Ver
`docs/` y `openspec/` para el contexto completo de investigación.

## Requisitos

- Python 3.12+
- Opcional: `CONNECTION_STRING` en `.env` (Postgres). Sin ella, usa SQLite
  local (`./catalogo.db`).

## Uso

```bash
python -m pip install -e ".[dev]"
python -m app.seed        # siembra la versión sintética si no existe
python -m pytest -q       # 8 pruebas sobre SQLite en memoria
python -m uvicorn app.main:app --reload   # http://127.0.0.1:8000/docs
```
