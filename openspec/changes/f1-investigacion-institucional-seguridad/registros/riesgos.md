# Registro de riesgos — Fase 1

## Metadatos del registro

- **Cambio:** `f1-investigacion-institucional-seguridad`.
- **Proyecto:** `psicotest-backend`.
- **Fecha de registro:** 2026-08-13.
- **Naturaleza:** investigación y documentación; no autoriza código, API, recolección ni avance de fase.
- **Estado de las puertas:** puertas 0 y 1 **NO APROBADAS**.
- **Criterio de evidencia:** solo se consideran enlazables los documentos de este repositorio. Las respuestas institucionales, autoridades, políticas y plazos que no estén documentados aquí permanecen pendientes.
- **Registros relacionados:** [decisiones.md](decisiones.md), [evidencia-faltante.md](evidencia-faltante.md), [datos.md](datos.md) y [descubrimiento.md](descubrimiento.md).

Los valores de impacto y probabilidad que dicen «potencial» o «pendiente» no son mediciones institucionales. Son una forma provisional de hacer visible el riesgo mientras la institución confirma el contexto, la autoridad y la evidencia necesaria.

## Entradas

### R-01 — Confusión del propósito exploratorio con una decisión

- **Daño:** una persona puede interpretar una afinidad como «la carrera correcta», una promesa o una decisión en lugar de orientación exploratoria plural, con razones, incertidumbre y limitaciones.
- **Población:** estudiantes de secundaria, postulantes y otras personas interesadas; participantes de investigación cuando corresponda.
- **Impacto:** potencialmente alto; requiere valoración institucional.
- **Probabilidad:** no estimada; requiere evidencia de comprensión y uso.
- **Mitigación:** mantener el propósito como propuesta pendiente; exigir salida plural, límites visibles y preguntas de siguiente paso; detener cualquier avance si la afinidad se presenta como decisión.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [docs/README.md](../../../../docs/README.md), [docs/04 — Plan de investigación](../../../../docs/04-research-plan.md), [spec.md — Propósito de orientación exploratoria y de bajo riesgo](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** PENDIENTE DE CONFIRMACIÓN; la aprobación de puerta 0 no está registrada.
- **Criterio de detención:** no avanzar si falta la aprobación verificable del propósito, el nivel de consecuencias o los límites de uso.
- **Tareas relacionadas:** 1.1, 1.3, 6.2.

### R-02 — Habilitación de usos prohibidos o de alto impacto

- **Daño:** admisión o matrícula automática, elegibilidad, éxito académico, empleabilidad, diagnóstico clínico o decisiones de alto impacto podrían atribuirse a una salida que solo se propone como exploratoria.
- **Población:** todas las personas que reciban o interpreten una salida futura, incluidos menores y postulantes.
- **Impacto:** potencialmente alto; el daño y las consecuencias deben ser revisados por la autoridad que la institución confirme.
- **Probabilidad:** no estimada; no existe implementación que permita medirla.
- **Mitigación:** registrar cada uso como prohibido; rechazar comportamientos que lo habiliten; no definir cortes, etiquetas definitivas ni reglas de elegibilidad en esta fase.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [docs/README.md](../../../../docs/README.md), [docs/02 — Modelo de perfil](../../../../docs/02-profile-model.md), [spec.md — Usos prohibidos registrados](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** CONTROL DOCUMENTADO; la confirmación institucional de propósito, consecuencias y autoridad sigue pendiente.
- **Criterio de detención:** detenerse ante cualquier propuesta de admisión, elegibilidad, diagnóstico, predicción determinista o decisión de alto impacto.
- **Tareas relacionadas:** 1.2, 1.3, 6.2.

### R-03 — Tratar poblaciones distintas como si fueran intercambiables

- **Daño:** extrapolar comprensión, consentimiento, lenguaje, accesibilidad, riesgos o resultados de una población a otra puede producir interpretaciones no respaldadas.
- **Población:** estudiantes de secundaria, postulantes, otras personas interesadas y participantes de investigación.
- **Impacto:** potencialmente alto; depende de la decisión de uso y de la población aprobada.
- **Probabilidad:** no estimada; falta marco muestral y evidencia por población.
- **Mitigación:** mantener secciones separadas por población; no derivar el tratamiento de menores del de adultos; declarar límites de generalización.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [docs/02 — Modelo de perfil](../../../../docs/02-profile-model.md), [docs/04 — Etapa 1](../../../../docs/04-research-plan.md), [spec.md — Poblaciones como grupos distintos](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** CONTROL DOCUMENTADO; población, condiciones de inclusión y generalización continúan pendientes.
- **Criterio de detención:** no generalizar ni iniciar recolección para una población cuyo tratamiento y salvaguardas no estén confirmados.
- **Tareas relacionadas:** 2.1, 2.2, 2.3, 6.2.

### R-04 — Salvaguardas insuficientes para menores

- **Daño:** recolectar o interpretar información de menores sin procedimiento específico de consentimiento/asentimiento, comprensión y acompañamiento puede afectar sus derechos y su seguridad.
- **Población:** estudiantes de secundaria y cualquier otra población menor que la institución incluya.
- **Impacto:** potencialmente alto; revisión institucional, ética y legal pendiente.
- **Probabilidad:** no estimada; el procedimiento aplicable no está documentado en el repositorio.
- **Mitigación:** investigar un protocolo específico que cubra edades, quién consiente, quién asiente, comprensión y acompañamiento; no asumir que el procedimiento de adultos es suficiente; no recolectar datos mientras la salvaguarda crítica esté pendiente.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [docs/01 — Privacidad y salvaguardas para menores](../../../../docs/01-psychometric-foundations.md), [docs/04 — Etapa 0](../../../../docs/04-research-plan.md), [spec.md — Consentimiento y asentimiento para menores](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** BLOQUEADO; falta protocolo específico con fuente y revisión institucional/legal.
- **Criterio de detención:** detener la investigación con menores si no existe protocolo aprobado y evidencia de comprensión, consentimiento/asentimiento y acompañamiento.
- **Tareas relacionadas:** 3.1, 3.4, 6.2.

### R-05 — Decidir gobierno de datos sin revisión institucional o legal

- **Daño:** recolectar más datos de los necesarios, separar de forma insuficiente identidad y respuestas, permitir acceso indebido o retener/eliminar información bajo reglas no autorizadas.
- **Población:** participantes de investigación y personas que eventualmente usen la orientación; también terceros cuyos datos pudieran quedar asociados.
- **Impacto:** potencialmente alto; la base aplicable y la responsabilidad competente están pendientes.
- **Probabilidad:** no estimada; no existe recolección ni política aprobada en este repositorio.
- **Mitigación:** mantener un mapa conceptual de finalidad, minimización, separación, retiro, acceso, retención, eliminación y solicitudes; marcarlo como PENDIENTE DE REVISIÓN institucional/legal; no fijar políticas ni plazos por inferencia.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [docs/01 — Administración, puntuación, reporte y privacidad](../../../../docs/01-psychometric-foundations.md), [docs/05 — Seguridad, privacidad y gobernanza](../../../../docs/05-stack-tecnologico-y-arquitectura.md), [spec.md — Gobierno de datos sujeto a revisión](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** BLOQUEADO; falta la ruta de revisión ética/institucional y privacidad/legal.
- **Criterio de detención:** no recolectar, publicar, exportar ni definir retención o eliminación hasta contar con revisión y decisión verificables.
- **Tareas relacionadas:** 3.2, 3.3, 3.4, 6.2.

### R-06 — Asumir accesibilidad, idioma, dispositivos o conectividad sin datos propios

- **Daño:** una barrera ajena al constructo puede afectar comprensión, participación o interpretación; una acomodación no verificada también puede fallar.
- **Población:** todas las poblaciones previstas, diferenciadas por contexto, idioma, discapacidad, dispositivo, conectividad y modalidad cuando corresponda.
- **Impacto:** potencialmente alto; debe revisarse por población y condición.
- **Probabilidad:** no estimada; no hay datos propios enlazables sobre dispositivos, conectividad, idioma o barreras.
- **Mitigación:** consultar a las áreas pertinentes; registrar como evidencia faltante cada dato sin fuente propia; no afirmar capacidad existente ni inventar barreras o acomodaciones.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [docs/01 — Equidad y accesibilidad](../../../../docs/01-psychometric-foundations.md), [docs/04 — Etapa 3](../../../../docs/04-research-plan.md), [spec.md — Accesibilidad y contexto de las poblaciones](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** PENDIENTE DE CONFIRMACIÓN; los datos propios requeridos están registrados como faltantes.
- **Criterio de detención:** detener la expansión de afirmaciones si una barrera material o una condición de acceso relevante no ha sido estudiada.
- **Tareas relacionadas:** 4.1, 4.2, 6.2.

### R-07 — Usar un catálogo no autorizado o resolver la discrepancia por conveniencia

- **Daño:** recomendar programas duplicados, ausentes, desactualizados o sin estado y vigencia verificables; la salida podría aparentar cobertura sin autoridad institucional.
- **Población:** toda persona que explore la oferta UAGRM.
- **Impacto:** potencialmente alto; afecta la trazabilidad y el alcance de cualquier recomendación.
- **Probabilidad:** la discrepancia documental entre las fuentes está registrada; la probabilidad del daño por uso indebido no está estimada.
- **Mitigación:** conservar [S29] como 18 facultades y 69 programas y [S30] como aproximadamente 80 entradas con repeticiones; no elegir una cifra oficial; buscar una fuente institucional autorizada, versionada, reconciliada y con identificadores estables; no recomendar desde una lista no reconciliada.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [docs/README.md — Evidencia institucional](../../../../docs/README.md), [docs/03 — Fuentes S29 y S30](../../../../docs/03-references-and-repositories.md), [docs/04 — Reconciliación del catálogo](../../../../docs/04-research-plan.md), [spec.md — Discrepancia de catálogo](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** CONTROL DOCUMENTADO y BLOQUEADO para recomendar; la fuente autorizada permanece pendiente.
- **Criterio de detención:** detener cualquier recomendación o reconciliación final si falta autoridad, versión, estado o identificador estable.
- **Tareas relacionadas:** 5.1, 5.2, 5.4, 6.2.

### R-08 — Convertir el escalonamiento de cobertura en un pre-filtro

- **Daño:** excluir de hecho programas o poblaciones de la oferta autorizada y presentar una estrategia operativa como si fuera una regla de recomendación.
- **Población:** toda la población de interés y todas las personas que consulten programas UAGRM.
- **Impacto:** potencialmente alto; reduce cobertura y puede introducir una restricción no autorizada.
- **Probabilidad:** no estimada; no existe implementación, pero el diseño exige prevenir esta interpretación.
- **Mitigación:** registrar la cobertura futura de TODA la oferta autorizada UAGRM; permitir escalonamiento por facultad o sitio únicamente como estrategia de investigación; no establecer pre-filtro obligatorio de recomendación.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [docs/04 — Cobertura y etapas](../../../../docs/04-research-plan.md), [docs/05 — Principios de diseño candidatos](../../../../docs/05-stack-tecnologico-y-arquitectura.md), [docs/06 — Límites de alcance futuro](../../../../docs/06-reparto-de-implementacion-por-fases.md), [spec.md — Cobertura de toda la oferta autorizada](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** CONTROL DOCUMENTADO; la decisión de cobertura de puerta 1 sigue pendiente.
- **Criterio de detención:** detener si una etapa de investigación se presenta como exclusión permanente o filtro obligatorio de afinidad.
- **Tareas relacionadas:** 5.3, 5.4, 6.2.

### R-09 — Confundir completitud documental con aprobación de puertas

- **Daño:** tratar la creación de registros o el marcado de tareas como autorización institucional, cierre de Fase 1 o permiso para implementar.
- **Población:** equipo del proyecto, áreas institucionales y futuras personas usuarias.
- **Impacto:** potencialmente alto; puede iniciar trabajo no autorizado y ocultar bloqueos.
- **Probabilidad:** no estimada; el riesgo se mantiene porque las puertas no están aprobadas.
- **Mitigación:** mantener estado `proposed`, puertas 0 y 1 NO APROBADAS, Fase 1 NO INICIADA; enlazar cada decisión con su evidencia y bloqueo; no actualizar `state.yaml` ni afirmar avance de producto.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [proposal.md](../proposal.md), [state.yaml](../state.yaml), [docs/06 — Reglas de coordinación](../../../../docs/06-reparto-de-implementacion-por-fases.md).
- **Estado:** CONTROL DOCUMENTADO; el riesgo no se considera resuelto por este apply documental.
- **Criterio de detención:** no iniciar software, API, infraestructura, recolección ni la siguiente fase por la sola completitud de tareas.
- **Tareas relacionadas:** 1.3, 2.3, 3.4, 5.4, 6.2.

### R-10 — Confundir la propiedad futura del contrato con un contrato existente

- **Daño:** incorporar propuestas del frontend como reglas o campos del dominio/API, o integrar contra un contrato no publicado ni versionado.
- **Población:** equipos de backend y frontend, y personas afectadas por una futura integración.
- **Impacto:** potencialmente medio o alto; depende de que se trate como comportamiento autorizado.
- **Probabilidad:** no estimada; actualmente no existe API ni contrato implementado.
- **Mitigación:** dejar documentado que el backend será propietario futuro del contrato de dominio/API; el frontend será consumidor solo después de publicación y versionado; no crear endpoints, campos ni reglas en esta fase.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL para la autorización futura.
- **Evidencia:** [docs/05 — Modelo de dos repositorios y contrato API](../../../../docs/05-stack-tecnologico-y-arquitectura.md), [docs/06 — Reglas de coordinación](../../../../docs/06-reparto-de-implementacion-por-fases.md), [spec.md — Propiedad futura del contrato](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** CONTROL DOCUMENTADO; no hay contrato publicado.
- **Criterio de detención:** no integrar ni representar como existente un contrato que el backend todavía no haya autorizado, publicado y versionado.
- **Tareas relacionadas:** 6.4.

### R-11 — Declarar bloqueo por falta de respuesta sin plazo institucional definido

- **Daño:** inferir aprobación por silencio o afirmar que un plazo venció cuando la institución todavía no definió ese plazo.
- **Población:** todas las decisiones críticas de puertas 0 y 1.
- **Impacto:** potencialmente alto; afecta autorización, trazabilidad y avance.
- **Probabilidad:** no estimada; no existe plazo institucional enlazable en el repositorio.
- **Mitigación:** registrar la regla de bloqueo como propuesta operativa: si no hay respuesta dentro del plazo que la institución defina, se bloquea y no se avanza; mantener el plazo y el estado de respuesta como pendientes; no afirmar vencimiento.
- **Responsable:** PENDIENTE DE CONFIRMACIÓN INSTITUCIONAL.
- **Evidencia:** [design.md — Decisión, cierre y coordinación](../design.md), [docs/04 — Criterios de detención](../../../../docs/04-research-plan.md), [spec.md — Cierre alineado a puertas 0 y 1](../specs/investigacion-institucional-seguridad/spec.md).
- **Estado:** BLOQUEADO para aplicar la regla a un caso concreto; la regla y el plazo institucional están pendientes.
- **Criterio de detención:** no avanzar por silencio; cuando exista un plazo institucional verificable y la falta de respuesta esté documentada, registrar el bloqueo correspondiente.
- **Tareas relacionadas:** 6.3, 6.2.

## Criterio general de escalamiento

Ante un riesgo material de propósito, uso prohibido, salvaguarda de menores, privacidad, accesibilidad, cobertura o autoridad institucional, **DEBE** estrecharse la afirmación, solicitarse evidencia, registrarse el bloqueo o detenerse el trabajo. **NO DEBE** cubrirse la incertidumbre con una interfaz, una cifra, un nombre, una política o una decisión inventada.
