"""Composición de la aplicación: crea la app FastAPI y monta los routers de
dominio. No contiene lógica de negocio ni de consulta — eso vive en cada
paquete de dominio (hoy solo `app.catalog`)."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.catalog.router import router as catalog_router

app = FastAPI(
    title="TestPsico — catálogo institucional",
    version="0.1.0",
    description=(
        "Prototipo de investigación. La oferta servida puede ser sintética: "
        "cada respuesta declara su procedencia en `catalog`. No expresa "
        "admisión, elegibilidad ni recomendación."
    ),
)

# Prototipo de investigación: el frontend aún no tiene dominio publicado.
# ponytail: origen abierto para desarrollo local, restringir cuando exista despliegue real.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(catalog_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
