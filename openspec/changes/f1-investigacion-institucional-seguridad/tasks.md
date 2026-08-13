# Tareas: Fase 1 — Investigación institucional y límites de seguridad

## Identidad del cambio

- project_id: `psicotest-backend` · cross_repo_change_id: `f1-investigacion-institucional-seguridad` · related_project: `psicotest-frontend` · responsable provisional: Marces.
- Contrato: backend propietario futuro del contrato de dominio/API; el frontend no lo inventa; lo consume solo publicado y versionado.
- NOTA: completar las tareas documenta la investigación; NO aprueba puertas 0–1 ni cierra Fase 1 del producto.

## Review Workload Forecast

Cambio documental: 0 líneas de código. Sin sdd-apply (decisión del usuario). Verificación: revisión documental; reversión: solo archivos del cambio.

Decision needed before apply: Yes
Chained PRs recommended: No
Chain strategy: pending
400-line budget risk: Low

## Workstream 1: Propósito y usos prohibidos

- [ ] 1.1 Consultar a Orientación Vocacional el propósito (exploratorio, bajo riesgo, salida plural); registrar `pregunta|respuesta|fuente/fecha|responsable|evidencia|decisión|bloqueo`. Evidencia: respuesta registrada. (PENDIENTE: respuesta institucional, fuente/fecha y responsable confirmado)
- [x] 1.2 Registrar en riesgos los usos prohibidos (admisión/matrícula automática, elegibilidad, éxito académico, empleabilidad, diagnóstico clínico, decisiones de alto impacto), sin comportamiento que los habilite. Evidencia: entrada con estado.
- [ ] 1.3 DECISIÓN: fijar qué evidencia satisface cada casilla de puerta 0 (propósito, prohibiciones, consecuencias); registrar estado. Dep: 1.1, 1.2. (PENDIENTE: decisión humana y evidencia de puerta 0)

## Workstream 2: Poblaciones y partes interesadas

- [x] 2.1 Documentar marco poblacional distinto (secundaria, postulantes, otras personas interesadas, participantes de investigación), sin extrapolar tratamientos. Evidencia: sección por población.
- [ ] 2.2 Consultar áreas (orientación, facultades, programas, accesibilidad, ética, registros, tecnología, privacidad); registrar mapa de interesados PENDIENTE DE CONFIRMACIÓN, sin nombres ni autoridades inventados. Evidencia: mapa por área. (PENDIENTE: consultas y responsables institucionales confirmados)
- [ ] 2.3 DECISIÓN: registrar qué evidencia confirma a cada responsable y qué casilla de puerta 1 depende de ello. Dep: 2.2. (PENDIENTE: confirmación de responsables y evidencia de puerta 1)

## Workstream 3: Datos y menores

- [ ] 3.1 Investigar procedimiento específico de consentimiento/asentimiento para menores (edades, quién consiente/asiente, verificación de comprensión, acompañamiento), sin derivarlo del de adultos. Evidencia: protocolo con fuente. (PENDIENTE: protocolo y revisión institucional/ética/legal)
- [x] 3.2 Documentar mapa de datos (finalidad, minimización, campos excluidos, separación identidad-respuestas, retiro, acceso, retención, eliminación, ruta de solicitudes) sujeto a revisión institucional/legal, sin fijar políticas ni plazos. Evidencia: estado pendiente.
- [ ] 3.3 Consultar a ética/investigación y privacidad/legal la ruta de revisión; registrar respuesta o su ausencia. Evidencia: consulta con fuente/fecha. (PENDIENTE: respuesta, fuente/fecha y responsable confirmado)
- [ ] 3.4 DECISIÓN: registrar qué evidencia satisface las casillas de puerta 1 sobre menores y privacidad. Dep: 3.1–3.3. (PENDIENTE: protocolo, revisión y decisión institucional)

## Workstream 4: Accesibilidad y contexto

- [ ] 4.1 Consultar y documentar idioma, cultura, discapacidad, dispositivos, conectividad y modalidades por población; barreras y acomodaciones solo con evidencia. Evidencia: respuestas con fuente/fecha. (PENDIENTE: respuestas institucionales y datos propios por población)
- [x] 4.2 Registrar como evidencia faltante todo dato sin fuente propia (p. ej., dispositivos/conectividad), sin afirmar capacidad existente. Evidencia: entradas en registro.

## Workstream 5: Catálogo [S29]/[S30] y cobertura

- [x] 5.1 Documentar discrepancia [S29] (18 facultades/69 programas) vs [S30] (~80 con repeticiones) sin elegir cifra oficial; fuente autorizada = evidencia faltante.
- [ ] 5.2 Consultar a tecnología/registros la fuente autorizada y versionada de la oferta; registrar resultado o bloqueo. Reconciliación: Fase 2. (PENDIENTE: consulta, fuente autorizada y responsable confirmado)
- [x] 5.3 Registrar que la cobertura futura alcanza TODA la oferta autorizada UAGRM; escalonamiento por facultad/sitio es estrategia, no pre-filtro. Evidencia: decisión con fuente.
- [ ] 5.4 DECISIÓN: registrar qué evidencia satisface la casilla de puerta 1 sobre cobertura/recomendación. Dep: 5.1–5.3. (PENDIENTE: fuente autorizada y decisión institucional de cobertura)

## Workstream 6: Riesgos, decisiones y cierre

- [x] 6.1 Consolidar registros de riesgos (daño, población, impacto/probabilidad, mitigación, responsable, evidencia, estado, detención), decisiones pendientes y evidencia faltante, vinculados. Evidencia: tres registros completos.
- [ ] 6.2 Revisar cada casilla de puertas 0–1: estado, decisión, autoridad, evidencia enlazable, fecha, dependencias. Dep: 1.3, 2.3, 3.4, 5.4, 6.1. (BLOQUEADA: decisiones y respuestas institucionales críticas pendientes)
- [ ] 6.3 BLOQUEO: institución sin respuesta en el plazo que ella defina (pendiente de definición) → registrar bloqueo; no inferir aprobación ni avanzar. Evidencia: bloqueo con fecha. (PENDIENTE: plazo institucional por definir y caso de falta de respuesta)
- [x] 6.4 Documentar declaración de contrato: backend propietario futuro del contrato dominio/API; frontend consumidor solo tras publicación/versionado; propuestas frontend no se incorporan. Evidencia: declaración en artefacto.
- [x] 6.5 Verificar que cada salida enlaza preguntas, respuestas, fuentes, decisiones, riesgos y bloqueos; español neutral/profesional (DEBE/NO DEBE/DEBERÍA/PUEDE). Evidencia: lista de verificación.

## Fuera del alcance

- Programación, diseño técnico, infraestructura, API, autenticación, base de datos: fuera de alcance (rechazar y registrar).
- Reconciliación del catálogo: Fase 2 del producto; no resolver aquí.
- Contrato de dominio/API: se diseña en fases futuras, previa autorización.
- No se lee ni modifica `psicotest-frontend`.
- Completar tareas no aprueba puertas 0–1 ni cierra Fase 1.

## Evidencia de unidad de trabajo documental

| Evidencia | Resultado exacto |
|---|---|
| Comando de prueba focalizada y resultado | **N/A — no existe runner ni código; cambio exclusivamente documental.** No se ejecutaron builds, tests ni comandos de proyecto, conforme al alcance de esta fase. La verificación se realizó mediante revisión de archivos y enlaces del paquete. |
| Comando/escenario de runtime y resultado | **N/A — no existe límite de runtime ni comportamiento ejecutable.** Las salidas son registros Markdown y actualización de casillas. |
| Límite de reversión | Revertir únicamente `tasks.md` y `registros/` dentro de este cambio (`riesgos.md`, `decisiones.md`, `evidencia-faltante.md`, `datos.md`, `descubrimiento.md`). `proposal.md`, `spec.md`, `design.md` y `state.yaml` no se modificaron. |
