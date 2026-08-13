# Diseño: Fase 1 — Investigación institucional y límites de seguridad

## Objetivos y alcance

Este documento diseña **cómo investigar, consultar, registrar, decidir y cerrar** la Fase 1 del producto. Las puertas 0 y 1 permanecen **NO APROBADAS**: este artefacto no las aprueba ni autoriza implementación. Se diseña la investigación de propósito, poblaciones, partes interesadas, menores, accesibilidad, gobierno de datos, usos prohibidos, cobertura UAGRM, discrepancia [S29]/[S30], riesgos, decisiones y evidencia faltante.

Quedan fuera código, tecnologías, API, entidades, infraestructura, datos, catálogo reconciliado e instrumento. Identidad: `project_id: psicotest-backend`; `cross_repo_change_id: f1-investigacion-institucional-seguridad`; relacionado: `psicotest-frontend`; responsable provisional: Marces. El backend será propietario futuro del contrato de dominio/API y el frontend será consumidor futuro; no podrá inventarlo.

## Workstreams

| Workstream | Entradas y actividades | Salidas |
|---|---|---|
| Propósito y usos | Contrastar orientación exploratoria, salida plural, prohibiciones y consecuencias de malinterpretación. | Propósito propuesto, límites, riesgos y aprobación pendiente. |
| Poblaciones y partes interesadas | Distinguir secundaria, postulantes, otras personas interesadas y participantes; confirmar áreas y autoridad real. | Marco poblacional y mapa por área, sin nombres inventados. |
| Datos y menores | Investigar consentimiento/asentimiento, comprensión, retiro, minimización, acceso, retención, eliminación y solicitudes. | Protocolo y mapa sujetos a revisión institucional/legal. |
| Accesibilidad y contexto | Consultar idioma, cultura, discapacidad, dispositivos, conectividad, modalidades y acomodaciones. | Evidencia confirmada, barreras y faltantes; sin supuestos. |
| Catálogo [S29]/[S30] | Conservar 18/69 frente a ~80 repetidas; buscar fuente autorizada sin elegir cifra ni resolver Fase 2. | Discrepancia y evidencia faltante de autoridad/versionado. |
| Riesgos y cierre | Consolidar registros y revisar cada casilla de puertas 0–1 con criterios de detención. | Estado respaldado o bloqueado, con trazabilidad. |

La decisión metodológica es trabajar por workstreams y registros vinculados, en lugar de un documento narrativo único: permite separar líneas de evidencia y detectar bloqueos. Toda incertidumbre se marca **PENDIENTE DE CONFIRMACIÓN**, en lugar de inferir una decisión por silencio.

## Plan de descubrimiento institucional

Las áreas candidatas de `proposal.md` y `docs/04` son todas **PENDIENTES DE CONFIRMACIÓN**. Se consultará la unidad o autoridad que la institución identifique, sin inventar nombres, cargos, atribuciones ni plazos.

| Área candidata | Agenda específica |
|---|---|
| Orientación Vocacional | Propósito, bajo riesgo, usos prohibidos, consecuencias y autoridad de aprobación. |
| Facultades y programas | Cobertura de toda la UAGRM, escalonamiento sin pre-filtro y fuentes de oferta. |
| Accesibilidad | Idioma, cultura, dispositivos, conectividad, barreras y acomodaciones. |
| Ética/investigación | Ruta de revisión, menores, consentimiento/asentimiento, comprensión y acompañamiento. |
| Registros | Poblaciones, reclutamiento, retiro, preguntas, correcciones y solicitudes. |
| Tecnología | Fuente autorizada, versionado y responsable institucional del catálogo; discrepancia [S29]/[S30]. |
| Privacidad/legal | Minimización, separación identidad-respuestas, acceso, retención, eliminación y base aplicable. |

Cada respuesta se registra como `pregunta | respuesta | fuente/fecha | responsable confirmado o PENDIENTE | evidencia | decisión | bloqueo`. La falta de respuesta es evidencia faltante, no consentimiento.

## Registros y mapa de datos

- **Riesgos:** daño, población, impacto/probabilidad, mitigación, responsable, evidencia, estado y criterio de detención.
- **Decisiones pendientes:** qué decidir, quién decide, evidencia necesaria, dependencia, estado y bloqueo.
- **Evidencia faltante:** casilla o afirmación, evidencia requerida, fuente buscada, fecha, responsable, impacto y próxima consulta.
- **Mapa de datos:** finalidad, minimización, campos excluidos, separación identidad/respuestas, retiro, acceso, retención, eliminación y ruta de solicitudes. Todo queda sujeto a revisión institucional/legal; no se fijan políticas ni plazos por inferencia. No se incorporan respuestas reales ni PII.

## Decisión, cierre y coordinación

Cada casilla de puertas 0 y 1 tendrá estado `pendiente`, `respaldada` o `bloqueada`, decisión explícita, autoridad/responsable confirmado, evidencia verificable enlazable, fecha y dependencias. Es bloqueo la evidencia crítica ausente, autoridad no confirmada, revisión pendiente o falta de respuesta dentro del plazo que la institución defina. Se detiene ante riesgo material, uso prohibido, salvaguarda o privacidad no resuelta, o escalonamiento convertido en pre-filtro. **No se infiere aprobación ni se avanza** por silencio o completitud documental.

El cambio futuro de `psicotest-frontend` usará el mismo `cross_repo_change_id`; este diseño no lee ni modifica ese repositorio ni crea artefactos frontend. El backend publicará y versionará el contrato solo tras autorización futura; el frontend lo consumirá entonces. No se diseñan contratos, endpoints, entidades ni tecnologías.

## Verificación, amenaza y preguntas abiertas

No hay migración, rollout ni runner de pruebas. La verificación es revisión documental: cada salida debe enlazar preguntas, respuestas, fuentes, decisiones, riesgos y bloqueos. **Threat Matrix: N/A — no existe routing, shell, subprocess, automatización VCS/PR, clasificación de ejecutables ni integración de procesos.**

Preguntas abiertas: [ ] responsables y autoridades reales; [ ] ruta ética/legal y menores; [ ] políticas y plazos de datos; [ ] accesibilidad y contexto; [ ] fuente autorizada del catálogo; [ ] plazo institucional para clasificar falta de respuesta como bloqueo. Todas siguen pendientes.
