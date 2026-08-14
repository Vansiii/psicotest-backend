# 07 — Contrato de dominio/API publicado por psicotest-backend

**Decisión primero:** este documento **sí** describe software que existe y corre, a diferencia de [01](./01-psychometric-foundations.md)–[06](./06-reparto-de-implementacion-por-fases.md), que son documentación de investigación. Cumple la regla 7 de [06](./06-reparto-de-implementacion-por-fases.md) («el backend publica el contrato de dominio/API; el frontend lo consume») y la condición de cierre de entrega («el backend no cierra la entrega hasta que su contrato esté documentado»).

**Versión del contrato:** `0.1.0` (`app.main:app.version`). **Fecha:** 2026-08-14.

> ⚠️ **Todo lo que sirve esta API es sintético.** Las decisiones [D-13 y D-14](../openspec/changes/f1-investigacion-institucional-seguridad/registros/decisiones.md) abrieron una vía de prototipo con datos marcados, **sin aprobar las puertas 0–1** de investigación institucional. Ninguna respuesta de esta API puede presentarse a una persona real en orientación mientras `is_synthetic` sea `true`. No expresa admisión, elegibilidad, éxito académico, empleabilidad ni diagnóstico.

## Reglas del contrato

1. **Solo el backend define estas formas.** El frontend las consume y no las redefine ni las amplía ([05 §7](./05-stack-tecnologico-y-arquitectura.md)).
2. **La procedencia viaja en cada respuesta.** Toda respuesta de dominio incluye un objeto `catalog` y/o `assessment` con `is_synthetic` y `source`. Un consumidor **DEBE** poder distinguir prototipo de dato autorizado sin consultar otra fuente.
3. **Inmutabilidad.** Una corrección se publica como versión nueva; no se edita una existente ([05 §6](./05-stack-tecnologico-y-arquitectura.md)). Un `TestSession` congela sus puntajes y afinidades al calcularlos: un cambio posterior de catálogo o cuestionario no reescribe un resultado ya emitido.
4. **Un único endpoint de escritura.** `POST /assessment/sessions`. El resto es lectura. No existen endpoints de edición ni borrado.
5. **El cliente no envía reglas.** No hay parámetro para pesos, fórmulas, perfiles ni carrera objetivo. Los filtros son metadatos explícitos y opcionales; **nunca** un pre-filtro obligatorio ([02](./02-profile-model.md)).

## Tipos compartidos

```jsonc
CatalogRef / AssessmentRef {
  "label": "sintetico-2026-01",     // identificador estable de la versión
  "source": "DATOS SINTÉTICOS…",     // procedencia legible
  "is_synthetic": true,              // obligatorio en toda respuesta
  "status": "publicada",             // "borrador" | "publicada"
  "effective_from": "2026-01-01"     // date | null
}

ProgramOut {
  "external_id": "SYN-001",          // ID estable; único dentro de una versión
  "name": "…",
  "faculty": "…",  "faculty_code": "FCET",
  "campus":  "…",  "campus_code":  "SC-CENTRAL",
  "level": "licenciatura",
  "modality": "presencial",
  "availability": "oferta_regular"
}
```

`faculty_code` y `campus_code` se exponen porque son los valores que aceptan los filtros de esta misma API: sin ellos el consumidor no puede construir una consulta filtrada a partir de una respuesta previa.

## Resolución de versión

Regla común a ambos dominios: **sin** parámetro de versión se sirve la **última publicada**; una versión en `borrador` solo se alcanza pidiéndola por `label`. Si no existe, `404`.

## Catálogo

| Método | Ruta | Parámetros | Respuesta |
|---|---|---|---|
| `GET` | `/catalog/versions` | — | `CatalogRef[]`, más reciente primero |
| `GET` | `/programs` | `catalog`, `faculty`, `campus`, `level`, `modality` (todos opcionales) | `ProgramList` |
| `GET` | `/programs/{external_id}` | `catalog` (opcional) | `ProgramDetail` |

```jsonc
ProgramList  { "catalog": CatalogRef, "count": 9, "programs": ProgramOut[] }

ProgramDetail extends ProgramOut {
  "catalog": CatalogRef,
  "profile": {                       // null si el programa no tiene perfil publicado
    "version": 1,
    "summary": "…",
    "activities": ["…"],
    "sources": ["…"],
    "limitations": "…",              // niega admisión, elegibilidad y pronóstico
    "reviewed_at": "2026-01-01"
  }
}
```

Sin filtros se devuelve **toda** la oferta de la versión: [02](./02-profile-model.md) prohíbe un pre-filtro obligatorio por facultad.

## Evaluación

| Método | Ruta | Cuerpo / Parámetros | Respuesta |
|---|---|---|---|
| `GET` | `/assessment/versions` | — | `AssessmentRef[]` |
| `GET` | `/assessment/questions` | `assessment` (opcional) | `QuestionList` |
| `POST` | `/assessment/sessions` | `SessionCreate` | `ResultOut` |
| `GET` | `/assessment/sessions/{session_id}` | — | `ResultOut` |

```jsonc
QuestionList { "assessment": AssessmentRef,
               "questions": [{ "id": 1, "text": "…", "domain_code": "analisis" }] }

SessionCreate {
  "assessment": null,                // label opcional
  "catalog": null,                   // label opcional
  "responses": [{ "question_id": 1, "value": 3 }]   // value entero 1..5
}

ResultOut {
  "session_id": "e4b7c18e…",         // uuid4 hex; enlace profundo compartible
  "assessment": AssessmentRef,
  "catalog": CatalogRef,
  "submitted_at": "2026-08-14T…",
  "domain_scores": [{ "domain_code": "analisis", "domain_name": "Análisis e investigación",
                      "raw_average": 3.0, "normalized": 0.5 }],
  "affinities":   [{ "relative_position": 1, "program": ProgramOut,
                     "affinity_score": 0.5532, "reasons": ["…"], "uncertainty": "…" }],
  "limitations": "…",                // texto fijo; el cliente no lo reescribe
  "exploration_prompts": ["…"]
}
```

### Reglas de puntuación y afinidad

- `normalized = (raw_average − 1) / 4`, es decir la escala 1–5 mapeada a 0–1.
- `affinity_score` = promedio ponderado de `normalized` por los pesos de dominio declarados para ese programa.
- **Un programa sin pesos declarados se excluye del resultado.** No se inventa una afinidad sin evidencia declarada.
- `relative_position` es un *dense rank* sobre el puntaje redondeado a 2 decimales: **los empates comparten posición** y quedan visibles, como exige [01 §6](./01-psychometric-foundations.md).
- La salida es **plural**: se devuelven todas las afinidades calculables, nunca «la carrera correcta».

> La fórmula es una heurística ilustrativa del prototipo, **no** una regla de puntuación validada. Sustituirla es condición para cualquier uso real ([01 §5–6](./01-psychometric-foundations.md)).

## Errores

| Código | Cuándo |
|---|---|
| `400` | Las respuestas no cubren exactamente el conjunto de preguntas de la versión (falta una, sobra una, o el `question_id` no pertenece). |
| `404` | Versión, programa o sesión inexistente. |
| `422` | Validación de esquema; p. ej. `value` fuera de 1–5. |

Formato: `{"detail": "mensaje en español"}` (estándar de FastAPI).

## Operación

- `GET /health` → `{"status": "ok"}`.
- Documentación viva generada: `/docs` (OpenAPI).
- CORS: orígenes `*`, métodos `GET` y `POST`. Abierto para desarrollo local; **restringir antes de cualquier despliegue** (marcado en `app/main.py`).
- Sin autenticación ni autorización. El prototipo no maneja identidad ni datos personales; habilitarlos exige las puertas de [05 §8](./05-stack-tecnologico-y-arquitectura.md).

## Compatibilidad y revocación

- Cambios aditivos (campo nuevo opcional, endpoint nuevo) no rompen al consumidor. Un cambio incompatible **DEBE** subir la versión del contrato y registrarse aquí.
- **Revocación:** si la institución aprueba un catálogo autorizado o un instrumento validado, las versiones sintéticas **DEBEN** dejar de publicarse (condición de D-13 y D-14).

## Enlaces

- [Decisiones D-13, D-14, D-15](../openspec/changes/f1-investigacion-institucional-seguridad/registros/decisiones.md)
- [05 — Arquitectura candidata](./05-stack-tecnologico-y-arquitectura.md) · [06 — Coordinación por fases](./06-reparto-de-implementacion-por-fases.md)
- Consumidor: [psicotest-frontend](../../frontend/README.md)
