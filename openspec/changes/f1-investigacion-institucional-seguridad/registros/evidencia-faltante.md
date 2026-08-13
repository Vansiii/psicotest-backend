# Registro de evidencia faltante — Fase 1

## Metadatos del registro

- **Cambio:** `f1-investigacion-institucional-seguridad`.
- **Proyecto:** `psicotest-backend`.
- **Fecha de registro:** 2026-08-13.
- **Estado global:** evidencia crítica pendiente; puertas 0 y 1 **NO APROBADAS**.
- **Regla de cierre:** un ítem solo se completa con evidencia institucional, ética, legal, de accesibilidad o de catálogo que sea verificable, enlazable, fechada y atribuible a una autoridad confirmada. No se aceptan inferencias desde el silencio.
- **Registros relacionados:** [riesgos.md](riesgos.md), [decisiones.md](decisiones.md), [datos.md](datos.md) y [descubrimiento.md](descubrimiento.md).

## Ítems

### E-01 — Respuesta institucional sobre el propósito

- **Ítem:** respuesta de Orientación Vocacional sobre propósito exploratorio, bajo riesgo, salida plural y consecuencias de interpretación.
- **Por qué importa:** es evidencia requerida para la casilla de propósito de puerta 0; el contexto de una página institucional no equivale a aprobación de TestPsico.
- **Fuente enlazable disponible:** [docs/README.md — Evidencia institucional](../../../../docs/README.md) y [docs/04 — Etapa 0](../../../../docs/04-research-plan.md).
- **Qué lo completaría:** consulta respondida, con fuente, fecha, responsable y decisión institucional verificable.
- **Estado:** PENDIENTE DE CONFIRMACIÓN.
- **Tareas:** 1.1, 1.3.

### E-02 — Criterios y decisión de la puerta 0

- **Ítem:** evidencia que satisface cada casilla de puerta 0: propósito, prohibiciones, consecuencias, privacidad, acceso, retención, eliminación y ausencia de ranking, corte o etiqueta definitiva.
- **Por qué importa:** documentar una propuesta no aprueba la puerta ni autoriza implementación.
- **Fuente enlazable disponible:** [proposal.md — Cierre medible](../proposal.md), [docs/01 — Puerta mínima](../../../../docs/01-psychometric-foundations.md), [docs/04 — Puerta 0](../../../../docs/04-research-plan.md).
- **Qué lo completaría:** decisión humana explícita, autoridad confirmada, evidencia enlazable y fecha para cada casilla.
- **Estado:** BLOQUEADO por E-01 y por decisiones institucionales pendientes.
- **Tareas:** 1.3, 6.2.

### E-03 — Responsables institucionales por área

- **Ítem:** responsables y atribuciones confirmados para orientación, facultades, programas, accesibilidad, ética/investigación, registros, tecnología y privacidad/legal.
- **Por qué importa:** una casilla de puerta 1 no puede tener autoridad inferida ni responsable inventado.
- **Fuente enlazable disponible:** [proposal.md — Áreas candidatas](../proposal.md), [design.md — Plan de descubrimiento](../design.md).
- **Qué lo completaría:** mapa institucional con unidad o autoridad, atribución, fuente, fecha y decisión confirmada.
- **Estado:** PENDIENTE DE CONFIRMACIÓN.
- **Tareas:** 2.2, 2.3.

### E-04 — Marco de población aprobado

- **Ítem:** decisión sobre inclusión y tratamiento diferenciado de secundaria, postulantes, otras personas interesadas y participantes de investigación.
- **Por qué importa:** las poblaciones no son intercambiables; la decisión cambia comprensión, consentimiento, accesibilidad, riesgo y generalización.
- **Fuente enlazable disponible:** [docs/02 — Propósito, población y contexto](../../../../docs/02-profile-model.md), [docs/04 — Etapa 1](../../../../docs/04-research-plan.md).
- **Qué lo completaría:** marco poblacional aprobado con condiciones de inclusión, salvaguardas y límites de generalización por grupo.
- **Estado:** PENDIENTE DE CONFIRMACIÓN.
- **Tareas:** 2.1, 2.3, 6.2.

### E-05 — Protocolo específico para menores

- **Ítem:** protocolo de consentimiento/asentimiento para menores que cubra edades, quién consiente, quién asiente, comprensión y acompañamiento.
- **Por qué importa:** los documentos exigen no derivar el procedimiento de menores del de adultos; la falta del protocolo bloquea la investigación con menores.
- **Fuente enlazable disponible:** [docs/01 — Privacidad y menores](../../../../docs/01-psychometric-foundations.md), [docs/04 — Producción de la Etapa 0](../../../../docs/04-research-plan.md), [spec.md — Menores](../specs/investigacion-institucional-seguridad/spec.md).
- **Qué lo completaría:** protocolo institucional/ético/legal con fuente, fecha, revisión y responsable confirmado.
- **Estado:** BLOQUEADO.
- **Tareas:** 3.1, 3.4, 6.2.

### E-06 — Ruta de revisión ética, institucional y de privacidad/legal

- **Ítem:** respuesta sobre quién revisa la investigación, qué procedimiento aplica y cómo se documentan consentimiento/asentimiento, privacidad y solicitudes.
- **Por qué importa:** sin ruta de revisión no se pueden fijar políticas de datos ni declarar satisfecha la puerta 1.
- **Fuente enlazable disponible:** [docs/03 — Contexto legal, inclusión y adaptación](../../../../docs/03-references-and-repositories.md), [docs/05 — Seguridad y gobernanza](../../../../docs/05-stack-tecnologico-y-arquitectura.md).
- **Qué lo completaría:** respuesta de las áreas confirmadas, con fuente, fecha, alcance, decisión y requisitos aplicables.
- **Estado:** PENDIENTE DE CONFIRMACIÓN.
- **Tareas:** 3.3, 3.4, 6.2.

### E-07 — Gobierno de datos y plazos

- **Ítem:** revisión institucional/legal de finalidad, minimización, campos excluidos, separación identidad-respuestas, retiro, acceso, retención, eliminación y ruta de solicitudes.
- **Por qué importa:** decidir una política sin base verificable puede producir recolección, acceso o conservación indebidos.
- **Fuente enlazable disponible:** [registros/datos.md](datos.md), [docs/01 — Administración y privacidad](../../../../docs/01-psychometric-foundations.md), [spec.md — Gobierno de datos](../specs/investigacion-institucional-seguridad/spec.md).
- **Qué lo completaría:** revisión y decisión documentadas; cualquier plazo debe provenir de la autoridad competente y no de una inferencia del proyecto.
- **Estado:** PENDIENTE DE REVISIÓN INSTITUCIONAL/LEGAL.
- **Tareas:** 3.2, 3.3, 3.4.

### E-08 — Datos propios de accesibilidad y contexto

- **Ítem:** datos o respuestas con fuente propia sobre idioma, cultura, discapacidad, dispositivos, conectividad, modalidades, barreras y acomodaciones por población.
- **Por qué importa:** sin datos propios no se puede afirmar capacidad existente, ausencia de barreras ni comparabilidad entre condiciones.
- **Fuente enlazable disponible:** [docs/01 — Equidad y accesibilidad](../../../../docs/01-psychometric-foundations.md), [docs/04 — Etapa 3](../../../../docs/04-research-plan.md), [spec.md — Escenario de contexto sin datos propios](../specs/investigacion-institucional-seguridad/spec.md).
- **Qué lo completaría:** consultas o estudios documentados con fuente, fecha, población, método y respuesta institucional; sin inventar barreras o acomodaciones.
- **Estado:** PENDIENTE DE CONFIRMACIÓN; no hay datos propios enlazables en este repositorio para estos aspectos.
- **Tareas:** 4.1, 4.2.

### E-09 — Fuente autorizada del catálogo UAGRM

- **Ítem:** catálogo institucional autorizado, versionado, reconciliado y con identificadores estables, estado y vigencia.
- **Por qué importa:** [S29] y [S30] tienen alcances distintos; ninguna cifra puede elegirse como catálogo oficial en esta fase.
- **Fuente enlazable disponible:** [docs/03 — S29 y S30](../../../../docs/03-references-and-repositories.md), [docs/04 — Evidencia inicial de catálogo](../../../../docs/04-research-plan.md).
- **Qué lo completaría:** fuente autorizada y versión institucional, responsable confirmado, fecha, método de reconciliación y registro de discrepancias.
- **Estado:** PENDIENTE DE CONFIRMACIÓN.
- **Tareas:** 5.1, 5.2, 5.4.

### E-10 — Decisión de cobertura y escalonamiento

- **Ítem:** decisión institucional que confirme cobertura de TODA la oferta autorizada UAGRM y defina el escalonamiento como estrategia, no como pre-filtro.
- **Por qué importa:** una estrategia por facultad o sitio no debe reducir silenciosamente el alcance de recomendación.
- **Fuente enlazable disponible:** [docs/04 — Cobertura por etapas](../../../../docs/04-research-plan.md), [docs/06 — Límites de alcance](../../../../docs/06-reparto-de-implementacion-por-fases.md).
- **Qué lo completaría:** catálogo autorizado y decisión de cobertura con responsables, límites, dependencias y fecha.
- **Estado:** PENDIENTE DE CONFIRMACIÓN.
- **Tareas:** 5.3, 5.4, 6.2.

### E-11 — Revisión consolidada de puertas 0 y 1

- **Ítem:** revisión casilla por casilla con estado, decisión, autoridad, evidencia enlazable, fecha y dependencias.
- **Por qué importa:** es la condición de cierre de la investigación; completar registros no la sustituye.
- **Fuente enlazable disponible:** [design.md — Decisión, cierre y coordinación](../design.md), [proposal.md — Cierre medible](../proposal.md).
- **Qué lo completaría:** revisión humana posterior a resolver o declarar bloqueadas las dependencias E-01 a E-10.
- **Estado:** BLOQUEADO.
- **Tareas:** 6.2.

### E-12 — Plazo institucional para falta de respuesta

- **Ítem:** definición del plazo institucional que permita clasificar una consulta crítica sin respuesta como bloqueo.
- **Por qué importa:** no se debe afirmar que un plazo venció ni inferir aprobación mientras el plazo no esté definido.
- **Fuente enlazable disponible:** [design.md — Decisión, cierre y coordinación](../design.md), [docs/04 — Criterios de detención](../../../../docs/04-research-plan.md).
- **Qué lo completaría:** regla institucional fechada y fuente de autoridad; después, registro de la consulta y de la respuesta o ausencia conforme a esa regla.
- **Estado:** PENDIENTE DE CONFIRMACIÓN; no se afirma vencimiento.
- **Tareas:** 6.3.

### E-13 — Autorización futura del contrato dominio/API

- **Ítem:** contrato de dominio/API publicado y versionado por el backend, junto con la autorización para que el frontend lo consuma.
- **Por qué importa:** evita integrar contra campos o reglas inventados por otro repositorio.
- **Fuente enlazable disponible:** [docs/05 — Contrato API conceptual](../../../../docs/05-stack-tecnologico-y-arquitectura.md), [docs/06 — Propiedad del contrato](../../../../docs/06-reparto-de-implementacion-por-fases.md).
- **Qué lo completaría:** cambio futuro autorizado, contrato documentado y versión verificable; este cambio documental no lo crea.
- **Estado:** PENDIENTE DE CONFIRMACIÓN FUTURA; no es una capacidad actual.
- **Tareas:** 6.4.
