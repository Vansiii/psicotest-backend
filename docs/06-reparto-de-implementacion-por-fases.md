# 06 — Mapa futuro de coordinación por fases

**Decisión primero:** este documento es un tablero futuro, no evidencia de implementación. Conserva seis responsables provisionales y sus posibles entregas, pero las seis fases están **NO INICIADAS** y solo podrán comenzar después de las puertas de investigación y las decisiones institucionales de [04 — Plan de investigación](./04-research-plan.md).

TestPsico se orienta a carreras y programas de toda la UAGRM. Estudiantes de secundaria, postulantes y otras personas interesadas son poblaciones previstas, sujetas a muestreo, comprensión, consentimiento/asentimiento, accesibilidad y aprobación. Facultad, campus o sitio, nivel, modalidad y disponibilidad son metadatos; una fase no puede convertirlos en un filtro obligatorio de recomendación.

No se afirma que existan código, datos de prueba sintéticos, perfiles, ítems, baremos, roles, comandos, pruebas, infraestructura, API, contratos o datos. Las personas y responsabilidades son provisionales y sirven para coordinar una implementación futura.

## Reglas de coordinación

1. **Una decisión de investigación precede a cada fase.** Completar un documento no marca una fase como lista.
2. **Dos repositorios independientes:** `psicotest-backend` y `psicotest-frontend`, cada uno con su propio alcance, revisión y artefactos.
3. **OpenSpec por repositorio:** cada cambio futuro tendrá sus propios artefactos en el `openspec/` del repositorio correspondiente; no se usará la beta independiente de Stores como línea base [S32][S33][S34].
4. **Engram por repositorio:** ya existen memorias de investigación curadas y separadas para `psicotest-frontend` y `psicotest-backend`, incluida la decisión de alcance de toda la UAGRM. La identidad determinista futura dentro de cada repositorio mediante `.engram/config.json` y un `project_name` explícito queda pendiente; no se ha creado ese archivo ni otro archivo local. Las memorias se redactan en español y no contienen credenciales, respuestas brutas, datos personales o contenido psicométrico no aprobado [S36][S37][S38].
5. **Guía portátil:** cada raíz tendrá un `AGENTS.md` compacto, independiente de Gentle AI, con propósito, seguridad, lectura, OpenSpec, Engram o degradación, convenciones verificadas, entrega y reporte de bloqueo [S35].
6. **Contrato cruzado:** un cambio que afecte a ambos repositorios usa el mismo ID de cambio cruzado, dos cambios OpenSpec, memorias separadas y enlaces recíprocos.
7. **Propiedad del contrato:** el backend publica el contrato de dominio/API; el frontend lo consume y prueba desde su perspectiva. Ninguno inventa la versión del otro.
8. **Sin fases automáticas:** una persona decide si se abre el siguiente trabajo después de revisar evidencia y bloqueos.
9. **Sin dependencia del entorno de ejecución de Gentle AI:** el trabajo no depende de personas, instrucciones, comandos slash, subagentes, recibos de revisión, identificadores `lineage`, lentes ni comandos internos de Gentle AI.
10. **Entrega verificable:** cada entrega futura debe indicar estado, alcance, versión de contrato, evidencia, riesgos, decisiones pendientes y siguiente acción.

## Estado general

| Fase futura | Responsable provisional | Estado | Condición mínima para considerar inicio |
| --- | --- | --- | --- |
| 1. Investigación institucional y límites de seguridad | Marces | **NO INICIADA** | Puertas 0 y 1 aprobadas. |
| 2. Catálogo y perfiles educativos | Trevor | **NO INICIADA** | Puerta 2 aprobada y fuente institucional autorizada. |
| 3. Evaluación, respuesta-proceso y accesibilidad | Jhamil | **NO INICIADA** | Puertas 2 y 3 aprobadas; población y modalidad definidas. |
| 4. Puntuación y evidencia psicométrica | Juan Carlos | **NO INICIADA** | Matriz de especificación y contenido con puerta 4; no hay baremo productivo asumido. |
| 5. Afinidades y contrato de recomendación | Piere | **NO INICIADA** | Evidencia de perfiles, puntuación y uso plural suficiente. |
| 6. Reporte, integración y validación | Ivan | **NO INICIADA** | Puertas 5–7 y decisión de implementación de bajo riesgo. |

Los nombres son coordinación provisional. No implican asignación laboral, calificación profesional, acceso a datos o autoridad para aprobar un uso.

## Límites de alcance futuro

| Tema | Regla |
| --- | --- |
| Propósito | Orientación exploratoria de bajo riesgo, con afinidades plurales, razones, incertidumbre, limitaciones y preguntas. |
| Catálogo | Toda la oferta UAGRM autorizada, reconciliada y versionada. La cobertura por facultad o sitio puede ser gradual. |
| Población | Estudiantes de secundaria, postulantes y otras personas interesadas, según población y salvaguardas aprobadas. |
| Metadatos | Facultad, sitio, nivel, modalidad y disponibilidad explican o filtran una solicitud explícita; no determinan aptitud ni se vuelven pre-filtro obligatorio. |
| Perfil | `program_profile` educativo, con fuentes, versión, revisión y límites de afirmación; no perfil de personalidad ni requisito de admisión. |
| Puntuación | Hipótesis de medición que requiere contenido, respuesta-proceso, precisión, equidad y validez. No existen normas ni cortes aprobados. |
| Salida | Conjunto u orden exploratorio; nunca “la carrera correcta”, admisión, elegibilidad, éxito, empleabilidad, diagnóstico o decisión de alto impacto. |
| Datos | Sin respuestas reales, PII, credenciales ni contenido no aprobado en documentación, memoria, datos de prueba o código futuro. |

## Entrega común entre repositorios

Cada fase futura que afecte ambos repositorios debe entregar dos paquetes relacionados:

```text
ID de cambio cruzado: por definir
├── psicotest-backend/openspec/changes/<cambio-backend>/
└── psicotest-frontend/openspec/changes/<cambio-frontend>/
```

Los nombres son ilustrativos y no indican que existan archivos. Cada paquete debe enlazar al otro y declarar:

- objetivo y alcance del cambio;
- puerta de investigación que lo habilita;
- contrato y versión que publica o consume;
- fuente de catálogo, perfil, puntuación o evidencia relevante;
- datos que se excluyen por privacidad;
- evidencia de validación pendiente o realizada;
- riesgos, bloqueos y decisión requerida;
- memoria de proyecto relacionada, sin usar Engram como fuente normativa.

El backend no cierra la entrega hasta que su contrato esté documentado. El frontend no integra contra un contrato imaginado. Si Engram no está disponible, ambos repositorios continúan desde `AGENTS.md`, OpenSpec y sus documentos y reportan la degradación.

## Fase 1 — Investigación institucional y límites de seguridad — Marces

**Estado: NO INICIADA.**

### Objetivo futuro

Dejar aprobados el propósito de bajo riesgo, las poblaciones, las partes interesadas, el gobierno de datos, el catálogo pendiente de reconciliación y los usos prohibidos antes de diseñar software.

### Trabajo candidato

- coordinar el descubrimiento con Orientación Vocacional, facultades, programas, accesibilidad, ética/investigación, registros y privacidad;
- definir estudiantes de secundaria, postulantes y otras personas interesadas como poblaciones distintas cuando corresponda;
- documentar consentimiento/asentimiento, retiro, minimización, acceso, retención, eliminación y ruta de preguntas;
- crear el mapa de riesgos y el límite explícito frente a admisión, éxito, empleabilidad, clínica y alto impacto;
- definir el marco de cobertura de toda la UAGRM y su estrategia gradual por facultad o sitio;
- preparar el cambio cruzado y los documentos raíz de ambos repositorios, sin inicializarlos hasta la autorización.

### Puerta y entrega

La salida requiere aprobación institucional y puertas 0–1. La entrega debe contener decisiones, responsables, fuentes, límites y bloqueos; no contiene una promesa de código, roles, infraestructura o comandos.

## Fase 2 — Catálogo y perfiles educativos — Trevor

**Estado: NO INICIADA.**

### Objetivo futuro

Reconciliar la oferta UAGRM y describir programas autorizados mediante `program_profile` revisados, sin inventar nombres, estados o disponibilidad.

### Trabajo candidato

- contrastar la información de admisiones —18 facultades y 69 programas en su alcance publicado— con la página de carreras —aproximadamente 80 entradas o páginas con repeticiones— [S29][S30];
- obtener una fuente institucional autorizada y documentar la discrepancia, sin elegir una cifra por conveniencia;
- asignar o registrar IDs estables, facultad, sitio, nivel, modalidad, disponibilidad, estado y fechas;
- crear perfiles educativos versionados con fuentes, revisión, disensos, accesibilidad y límites de afirmación;
- publicar el contrato de catálogo que el backend poseerá y que el frontend consumirá;
- dejar fuera cualquier programa cuya autoridad, estado o vigencia no esté resuelta.

### Puerta y entrega

La salida requiere puerta 2. El backend futuro sería dueño de la instantánea versionada y su contrato; el frontend recibiría solo una versión publicada. Un cambio de catálogo debe enlazar ambos repositorios si modifica presentación o filtros.

## Fase 3 — Evaluación, respuesta-proceso y accesibilidad — Jhamil

**Estado: NO INICIADA.**

### Objetivo futuro

Diseñar y estudiar una experiencia de evaluación comprensible, accesible y apropiada para las poblaciones aprobadas, sin afirmar que ya existe un instrumento.

### Trabajo candidato

- convertir la matriz de especificación aprobada en contenido original y versionado;
- estudiar instrucciones, comprensión, respuesta-proceso, idioma, dispositivos, conectividad y modalidades;
- investigar procedimientos de consentimiento/asentimiento y acompañamiento para menores o jóvenes cuando correspondan;
- definir manejo de faltantes, interrupciones y acomodaciones como decisiones de investigación;
- entregar al backend la especificación aprobada y al frontend los requisitos de interacción accesible;
- documentar qué evidencia aún falta antes de publicar una versión.

### Puerta y entrega

La salida requiere puerta 3 y contenido aprobado por la puerta 4. No incluye ítems reales, cantidades, roles, tiempos, API ni resultados no verificados. Las pruebas futuras se definirán con la modalidad y herramientas realmente elegidas.

## Fase 4 — Puntuación y evidencia psicométrica — Juan Carlos

**Estado: NO INICIADA.**

### Objetivo futuro

Estudiar transformaciones reproducibles de respuestas a dominios y su incertidumbre, manteniendo la puntuación separada del motor de afinidades.

### Trabajo candidato

- formalizar la regla de puntuación solo después de definir constructos y la matriz de especificación;
- estudiar confiabilidad, precisión, faltantes, estructura, subgrupos y límites de generalización;
- distinguir cualquier ejemplo o referencia sintética de una norma UAGRM;
- conservar versión, población, modalidad, evidencia y supuestos;
- publicar al backend un contrato de puntuación para que el motor de afinidades lo consuma sin elegir programas;
- entregar evidencia negativa, mixta y faltante, no solo resultados favorables.

### Puerta y entrega

La salida requiere puerta 4 y evidencia suficiente de la puerta 6 para el uso declarado. No autoriza percentiles, cortes, elegibilidad, éxito, empleabilidad, diagnóstico ni diferencias por factores contextuales sin evidencia y decisión específica.

## Fase 5 — Afinidades y contrato de recomendación — Piere

**Estado: NO INICIADA.**

### Objetivo futuro

Comparar dominios versionados con todos los perfiles autorizados y generar una salida plural, explicable y prudente.

### Trabajo candidato

- definir cómo el servidor selecciona el conjunto autorizado de programas sin pre-filtro obligatorio de facultad;
- mantener facultad, sitio, nivel, modalidad y disponibilidad como contexto o filtros explícitos;
- producir afinidades múltiples o un orden exploratorio con empates e incertidumbre visibles;
- asociar cada razón con dominio, perfil, fuente, evidencia y limitación;
- incluir preguntas para verificar actividades, modalidad, sitio, disponibilidad y conversación con orientación;
- rechazar reglas, pesos, perfiles o fórmulas arbitrarias enviadas por el frontend;
- documentar el contrato backend y los requisitos de presentación frontend.

### Puerta y entrega

La salida requiere evidencia de interpretación y uso exploratorio, no solo una función que ordene números. El frontend no puede convertir el resultado en admisión, elegibilidad o diagnóstico. Las reglas futuras deben ser revisadas y versionadas en el backend.

## Fase 6 — Reporte, integración y validación — Ivan

**Estado: NO INICIADA.**

### Objetivo futuro

Verificar que el flujo cruzado presenta el propósito, las afinidades, razones, incertidumbre, límites y preguntas de forma accesible y no excede la evidencia.

### Trabajo candidato

- integrar el contrato backend con la experiencia frontend mediante el ID de cambio cruzado;
- verificar estados de faltantes, ausencia de catálogo, baja disponibilidad, empate e incertidumbre;
- revisar que el reporte no agregue afirmaciones que no estén en `recommendation_result`;
- evaluar accesibilidad, privacidad, control de acceso, retención y ruta de soporte;
- documentar evidencia de integración, defectos, riesgos, decisión de publicación y condiciones de pausa;
- confirmar que ninguna prueba o dato futuro use respuestas reales sin aprobación, consentimiento y política de datos.

### Puerta y entrega

La salida requiere puertas 5–7 y una decisión explícita de operación de bajo riesgo. La integración no prueba validez por sí sola ni habilita fases de mayor impacto.

## Convenciones futuras de entrega

Cada responsable futuro entregará:

1. **Estado:** `listo`, `listo con riesgo` o `bloqueado`, solo con evidencia.
2. **Alcance:** qué se hizo y qué quedó fuera.
3. **Contrato:** versiones, campos, estados y límites que el consumidor puede usar.
4. **Evidencia:** procedimiento real, fecha, salida o artefacto verificable cuando existan.
5. **Datos:** fuentes, proveniencia, minimización y marcadores sintéticos si corresponden.
6. **Riesgos:** hallazgos negativos, incertidumbres y decisiones humanas pendientes.
7. **Cambio cruzado:** ID común, enlaces a ambos OpenSpec y memoria de cada proyecto.
8. **Siguiente acción:** una acción concreta, nunca una fase automática.

La futura guía `AGENTS.md` de cada repositorio debe documentar esta entrega, el orden de lectura y la degradación si Engram no está disponible. Debe excluir la persona y los mecanismos propios de Gentle AI; las memorias de investigación externas ya existentes no sustituyen esa guía ni la documentación normativa.

## Matriz futura de contratos

| Contrato | Dueño futuro | Consumidor futuro | Estado |
| --- | --- | --- | --- |
| Propósito, población y límites | Marces, sujeto a aprobación institucional | Todas las fases | No iniciado. |
| Catálogo, perfiles y disponibilidad | Backend, con insumos de Trevor | Afinidades y frontend | No iniciado. |
| Evaluación y respuesta-proceso | Coordinación de Jhamil, con contratos por repositorio | Puntuación y frontend | No iniciado. |
| Puntuación y evidencia | Backend, con trabajo de Juan Carlos | Afinidades y reporte | No iniciado. |
| Afinidades y explicación | Backend, con trabajo de Piere | Frontend e integración | No iniciado. |
| Reporte y validación cruzada | Ivan, con ambos repositorios | Decisión institucional | No iniciado. |

## Decisiones que bloquean el tablero

- aprobación institucional del propósito y población;
- catálogo autorizado, reconciliado y versionado;
- plan muestral que distinga cobertura por etapas de filtro de recomendación;
- procedimiento para menores y jóvenes cuando corresponda;
- constructos, matriz de especificación, contenido original y evidencia;
- forma de salida plural, incertidumbre y preguntas de exploración;
- privacidad, consentimiento/asentimiento, retención, eliminación y acceso;
- pila tecnológica real y capacidad de mantenimiento;
- contrato backend/frontend y estrategia de compatibilidad;
- criterio de publicación, monitoreo, revalidación y pausa.

Mientras una decisión siga abierta, se elige el comportamiento más restrictivo: no inventar datos, no publicar recomendaciones, conservar el resultado como investigación, hacer visibles los límites y registrar el bloqueo.

## Lista de verificación de coordinación futura

- [ ] La fase tiene una puerta de investigación aprobada.
- [ ] El cambio backend y frontend tiene el mismo ID cruzado cuando corresponde.
- [ ] Cada repositorio conserva su propio OpenSpec y mantiene separadas sus memorias de investigación externas en Engram.
- [ ] Las memorias no contienen datos de participantes, credenciales ni contenido no aprobado.
- [ ] `AGENTS.md` explica lectura, seguridad, pruebas reales y reporte de bloqueos.
- [ ] El backend publica el contrato y el frontend consume una versión identificable.
- [ ] La entrega incluye evidencia, incertidumbre, límites y decisiones pendientes.
- [ ] La salida mantiene pluralidad y no afirma una carrera correcta.
- [ ] No se agregaron fases automáticas ni dependencias de Gentle AI.
- [ ] Ninguna fase se cambia de **NO INICIADA** sin evidencia y autorización; completar una lista no es suficiente.

## Enlaces de contexto

- [README de documentación](./README.md)
- [04 — Plan de investigación](./04-research-plan.md)
- [05 — Arquitectura candidata](./05-stack-tecnologico-y-arquitectura.md)
- [02 — Modelo de perfil](./02-profile-model.md)
- [03 — Referencias y repositorios](./03-references-and-repositories.md)
