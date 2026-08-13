# 05 — Arquitectura candidata y decisiones técnicas para la etapa de investigación

**Decisión primero:** este documento no describe un sistema existente ni autoriza a programarlo. Es un registro de arquitectura candidata para dos repositorios independientes y actualmente vacíos: `psicotest-frontend` y `psicotest-backend`. Ninguna fase está en curso.

La arquitectura futura debe servir a una orientación vocacional/educativa de bajo riesgo para carreras y programas de toda la UAGRM. La salida será plural y exploratoria: afinidades, razones, incertidumbre, limitaciones y preguntas de siguiente paso. Facultad, campus o sitio, nivel, modalidad y disponibilidad serán metadatos del catálogo y filtros opcionales explícitos; no habrá un pre-filtro obligatorio de facultad.

La implementación futura solo podrá comenzar después de las puertas de investigación de [04 — Plan de investigación](./04-research-plan.md). Las decisiones de tecnología, entidades, endpoints, infraestructura y pruebas que aparecen aquí son hipótesis o contratos por validar, no capacidades ya existentes.

## Estado actual y decisiones de investigación

| Área | Estado |
| --- | --- |
| Repositorios | `psicotest-frontend` y `psicotest-backend` son repositorios Git separados, sin código ni commits según el estado de trabajo conocido. |
| OpenSpec | Cada repositorio tendrá su propio `openspec/` cuando la implementación sea autorizada. No se ha inicializado ninguno. |
| Engram | Ya se usan memorias de investigación curadas y separadas para `psicotest-frontend` y `psicotest-backend`, incluida la decisión de alcance de toda la UAGRM. No se ha creado `.engram/config.json` ni otro archivo local; la identidad determinista futura por repositorio mediante ese archivo y un `project_name` explícito queda pendiente. No es almacén normativo, de privacidad ni de respuestas. |
| `AGENTS.md` | Cada repositorio tendrá una guía raíz compacta y portable. No se crea en esta etapa. |
| Pila tecnológica | No seleccionada. Las tecnologías de este documento son candidatas para evaluación. |
| API y dominio | No existen. El backend será dueño del contrato futuro; el frontend lo consumirá. |
| Datos, perfiles e instrumento | No existen datos de prueba, conteos, perfiles, roles, resultados o baremos aprobados. |
| Fases | No iniciadas. La coordinación futura se describe en [06 — Reparto de implementación por fases](./06-reparto-de-implementacion-por-fases.md). |

## Principios de diseño candidatos

1. **Investigación antes de autoridad:** ninguna puntuación, catálogo o prototipo adquiere validez por estar implementado.
2. **Toda la oferta autorizada:** el catálogo de comparación debe cubrir toda la UAGRM que la institución autorice; la recolección puede escalonarse por facultad o sitio sin convertirlo en filtro obligatorio.
3. **Salida plural y prudente:** varias afinidades u orden exploratorio, razones, incertidumbre, límites y preguntas de exploración; nunca una única carrera correcta.
4. **Separación de evidencias:** catálogo institucional, perfiles educativos, medición psicométrica y evidencia de uso mantienen fuentes y versiones distintas.
5. **Backend como autoridad:** contratos de dominio, publicación, permisos y reglas versionadas pertenecen al backend; el frontend no inventa puntuaciones, perfiles ni reglas.
6. **Versionado e inmutabilidad:** una nueva oferta, perfil, medida, regla o reporte crea una versión identificable; no se modifica silenciosamente un resultado histórico.
7. **Privacidad por diseño:** Engram y los registros no contienen respuestas brutas, datos identificables ni contenido psicométrico no aprobado.
8. **Portabilidad:** un agente sin Gentle AI debe poder entender y operar cada repositorio leyendo su documentación, OpenSpec y políticas locales.
9. **Degradación explícita:** si Engram no está disponible, el trabajo continúa con `AGENTS.md`, OpenSpec, README y documentación del repositorio, y se informa la capacidad faltante.
10. **Sin copia de infraestructura propietaria:** no se incorporan personas, instrucciones, subagentes, registros, recibos, identificadores `lineage`, lentes ni comandos internos de Gentle AI.

## 1. Modelo de dos repositorios

### `psicotest-backend`

Responsabilidad futura candidata:

- dominio y contratos de catálogo, perfiles, evaluación, puntuación y afinidades;
- API, autorización, persistencia y auditoría;
- versionado de reglas y resultados;
- exportaciones de investigación aprobadas;
- documentación normativa del backend y su `AGENTS.md`.

No debe asumir que el frontend puede enviar pesos, fórmulas, perfiles, claves de respuesta o reglas arbitrarias.

### `psicotest-frontend`

Responsabilidad futura candidata:

- interfaz accesible de orientación, administración y reporte;
- consumo de contratos publicados por el backend;
- presentación de afinidades, razones, incertidumbre, límites y preguntas de exploración;
- manejo visible de errores, faltantes, accesibilidad y disponibilidad;
- documentación normativa del frontend y su `AGENTS.md`.

No debe reimplementar puntuación, inferencia, pertenencia de catálogo ni autorización.

### Estructura futura orientativa

```text
psicotest-backend/
├── AGENTS.md                         # guía portátil futura, no creada
├── openspec/                         # almacén propio futuro, no inicializado
├── .engram/config.json               # identidad futura, no creada
├── docs/
├── src/                              # estructura por decidir
└── tests/                            # pruebas; estrategia por decidir

psicotest-frontend/
├── AGENTS.md                         # guía portátil futura, no creada
├── openspec/                         # almacén propio futuro, no inicializado
├── .engram/config.json               # identidad futura, no creada
├── docs/
├── src/                              # estructura por decidir
└── tests/                            # pruebas; estrategia por decidir
```

La estructura no implica que existan esos directorios ni que cada uno sea un servicio. OpenSpec vive normalmente dentro de un repositorio; para TestPsico se elige un almacén independiente por repositorio y no la beta independiente de Stores [S32][S33][S34].

## 2. Orden de lectura para agentes portables

Cada `AGENTS.md` futuro debe indicar este orden, ajustado al repositorio:

1. `AGENTS.md` de la raíz: propósito, límites de seguridad, alcance del repositorio, reglas de trabajo y reporte de bloqueos.
2. `README.md` y documentación raíz: cómo orientarse y cuál es el estado real.
3. Documentos de investigación y arquitectura enlazados: requisitos psicométricos, catálogo, privacidad y límites.
4. `openspec/specs/`: comportamiento acordado vigente del repositorio.
5. `openspec/changes/<nombre>/`: propuesta, deltas, diseño y tareas del cambio que se trabaja.
6. Código y pruebas existentes, solo después de confirmar que realmente existen y que el cambio tiene autoridad.
7. Engram del proyecto: decisiones y descubrimientos curados, recuperados progresivamente y contrastados con documentos normativos.

La guía debe explicar que `openspec/specs/` expresa comportamiento acordado y que `openspec/changes/<nombre>/` expresa trabajo propuesto [S32]. Las propuestas, deltas de especificación, diseño y tareas deben revisarse antes de modificar comportamiento [S33]. También debe indicar que los comandos y las pruebas solo se documentan cuando existan y estén verificados, y que toda entrega informa finalización o bloqueo.

### Degradación de memoria

Ya se usan memorias de investigación curadas en Engram, separadas para los proyectos `psicotest-frontend` y `psicotest-backend`, incluida la decisión de alcance de toda la UAGRM [S36][S38]. La identidad determinista futura dentro de cada repositorio se definirá mediante `.engram/config.json`; ese archivo y cualquier otro archivo local de Engram siguen pendientes. `scope: project` es una convención semántica de búsqueda, no una frontera de privacidad [S37]. La sincronización puede exportar observaciones de proyecto y personales, por lo que no se deben guardar allí credenciales, respuestas brutas, datos identificables, datos de contacto, resultados individuales ni contenido psicométrico no aprobado.

Si Engram no está disponible:

- no se inventa memoria ni se bloquea silenciosamente;
- se continúa desde `AGENTS.md`, OpenSpec, README y documentos del repositorio;
- se informa en la entrega que la continuidad contextual no estuvo disponible;
- OpenSpec, Git y la documentación siguen siendo la fuente normativa.

## 3. Coordinación entre repositorios

Un cambio que afecte a ambos repositorios debe tener un **mismo ID de cambio cruzado**, aunque sus artefactos sean independientes.

| Regla | Backend | Frontend |
| --- | --- | --- |
| Artefactos OpenSpec | Cambio propio en su `openspec/changes/<nombre>/`. | Cambio propio en su `openspec/changes/<nombre>/`. |
| ID cruzado | Registra el ID compartido y enlaza el cambio frontend. | Registra el ID compartido y enlaza el cambio backend. |
| Contrato | El backend publica y versiona el contrato de dominio/API. | El frontend consume una versión publicada y no la redefine. |
| Engram | Memorias de investigación externas en el proyecto Engram backend, con enlace al cambio cruzado. | Memorias de investigación externas en el proyecto Engram frontend, con enlace al cambio cruzado. |
| Entrega | Entrega esquemas, estados, versiones, límites y evidencia. | Entrega consumo, accesibilidad, errores visibles y evidencia de compatibilidad. |
| Bloqueo | Si el contrato no está aprobado, no se simula como existente. | Si el contrato no está publicado, no se integra contra una suposición. |

Los enlaces recíprocos deben incluir alcance, versión de contrato, dependencias, decisiones pendientes y evidencia. Un cambio frontend no puede cerrar un cambio backend ni al revés. No hay fases automáticas: cada repositorio requiere revisión y decisión de avance.

## 4. Arquitectura candidata por responsabilidades

```text
[Persona]
    ↓
[Frontend accesible]
    ↓ contrato versionado
[Backend: casos de uso y autorización]
    ├── [Catálogo y perfiles educativos]
    ├── [Evaluación y respuestas protegidas]
    ├── [Puntuación versionada]
    ├── [Afinidades plurales y explicables]
    ├── [Reporte y auditoría]
    └── [Exportación de investigación aprobada]
```

### Separaciones necesarias

- **Catálogo:** determina programas autorizados, metadatos, estado y vigencia; no prueba la validez de una puntuación.
- **`program_profile`:** describe el programa y sus fuentes; no describe una persona ideal.
- **Evaluación:** conserva respuestas y condiciones de administración bajo políticas aprobadas.
- **Puntuación:** transforma respuestas según una versión definida; no elige programas.
- **Motor de afinidades:** compara dominios con perfiles autorizados y produce varias opciones, razones, incertidumbre y límites; no recibe reglas arbitrarias del cliente.
- **Reporte:** presenta el resultado sin añadir afirmaciones nuevas.
- **Analítica:** investiga conjuntos de datos aprobados; no escribe producción automáticamente.

## 5. Pila tecnológica candidata

No se adopta ninguna tecnología hasta que exista una decisión de alcance, un criterio de mantenimiento, una revisión de seguridad y una necesidad demostrada.

| Área | Candidatos a evaluar | Pregunta de investigación |
| --- | --- | --- |
| Frontend | React/TypeScript y un marco de trabajo web con renderizado accesible | ¿Permite la modalidad, accesibilidad, internacionalización y soporte institucional requeridos? |
| Backend | Python con un marco de trabajo HTTP y validación de esquemas, u otra alternativa | ¿Permite contratos claros, análisis reproducible, seguridad y mantenimiento local? |
| Persistencia | PostgreSQL u otra base relacional | ¿Protege versiones, relaciones de catálogo, minimización y auditoría? |
| Objetos | Almacenamiento compatible con objetos, si se necesita reporte | ¿Qué cifrado, permisos, retención y eliminación se requieren? |
| Identidad | Proveedor institucional compatible con estándares | ¿Quién autoriza usuarios y cómo se separan funciones sin inventar roles? |
| Análisis | R, Python u otra herramienta reproducible | ¿Cómo se preservan datos aprobados, parámetros, incertidumbre y revisión? |
| Calidad | Herramientas de formato, tipos, pruebas y accesibilidad | ¿Cuáles existen realmente y cuáles son proporcionales al alcance? |
| Operación | Entorno local y despliegue administrado por decidir | ¿Qué soporte, copias de seguridad, monitoreo y recuperación puede sostener la institución? |

No se declara que existan comandos, CI, contenedores, migraciones, roles, API, datos de prueba, infraestructura o pruebas hasta que una fase autorizada los cree y verifique.

## 6. Modelo conceptual de datos

Los siguientes nombres son hipótesis de vocabulario. No son migraciones ni entidades existentes.

| Entidad candidata | Propósito | Límite |
| --- | --- | --- |
| `institution` | Identidad de la institución y gobernanza del catálogo | No crea equivalencia entre instituciones. |
| `faculty`, `campus` / `site` | Metadatos de cobertura y contexto | No son filtros psicométricos obligatorios. |
| `program` | Carrera o programa autorizado | Solo aparece con fuente, estado y versión válidos. |
| `program_catalog_version` | Instantánea autorizada del catálogo | Debe conservar fuente, vigencia, IDs y reconciliación. |
| `program_profile` | Descripción educativa versionada | No expresa aptitud individual ni admisión. |
| `assessment_version` | Versión de contenido y matriz de especificación | Solo se publica después de puertas de investigación. |
| `session`, `response` | Condiciones y respuestas mínimas de administración | Separadas de identidad; consentimiento y retención pendientes. |
| `score` | Dominios y precisión de una versión de puntuación | No selecciona programas. |
| `recommendation_result` | Afinidades plurales, razones, evidencia y límites | No es decisión, diagnóstico ni pronóstico. |
| `evidence` | Fuente, población, uso, resultado e incertidumbre | Puede estar preliminar, mixta, faltante o no establecida. |
| `audit_event` | Trazabilidad mínima de acciones autorizadas | No guarda respuestas, credenciales ni PII innecesaria. |

Un resultado histórico futuro deberá conservar catálogo, perfiles, evaluación, puntuación, población, modalidad, evidencia, incertidumbre y límites que lo originaron. Cambiar la oferta o un perfil no debe reescribir silenciosamente la historia.

## 7. Contrato API conceptual

No existen endpoints actuales. Si una API se aprueba, el backend debe ser la fuente del contrato, documentarlo en su repositorio y entregar una versión consumible al frontend.

Un contrato futuro debería responder, como mínimo:

- qué catálogo y versión se consultan;
- qué programas están autorizados, con facultad, sitio, nivel, modalidad y disponibilidad;
- qué versión de perfil y evidencia respalda cada afinidad;
- qué población, condiciones y modalidad acompañan la puntuación;
- qué razones, incertidumbre, limitaciones y preguntas de exploración se muestran;
- qué errores, faltantes, estados y ausencia de evidencia debe presentar la interfaz;
- qué datos no se devuelven: respuestas protegidas, claves, reglas internas, credenciales y datos de otras personas.

El frontend no puede enviar pesos, fórmulas, perfiles, filtros ocultos, instrucciones para alterar la decisión ni datos para convertir una afinidad en elegibilidad. Los nombres de rutas, formatos de error, autenticación, idempotencia y versiones quedan pendientes de una decisión del backend.

## 8. Seguridad, privacidad y gobernanza candidatas

- **Finalidad y minimización:** recolectar solo lo necesario para orientación exploratoria aprobada.
- **Autorización:** definir acceso por función y necesidad, sin asumir roles de producto o calificaciones profesionales antes de la decisión institucional.
- **Separación:** mantener identidad restringida separada de respuestas, puntuaciones y resultados.
- **Versionado:** auditar publicación, cambios, acceso, exportación y revocación sin guardar contenido innecesario.
- **Transparencia:** mostrar propósito, fuente, versión, condiciones, razones, incertidumbre y límites.
- **Accesibilidad:** probar el flujo completo, no solo componentes aislados.
- **Menores y jóvenes:** aplicar el procedimiento aprobado de comprensión, consentimiento/asentimiento, acompañamiento y protección.
- **Datos sensibles:** no incluir respuestas reales o identificables en código, datos de prueba, registros, OpenSpec ni Engram.
- **Sin LLM como autoridad:** cualquier uso futuro de modelos generativos requeriría una decisión y validación separadas; no debe producir puntuación, afinidad, regla o afirmación sin control determinista y revisión.

Las obligaciones legales e institucionales deben revisarse con UAGRM y profesionales competentes; [S24] es un insumo de diseño, no asesoría legal.

## 9. Pruebas y reproducibilidad como hipótesis

Cuando exista código, el plan de calidad deberá definir pruebas proporcionales para:

- determinismo con las mismas entradas y versiones;
- inmutabilidad de catálogo, perfiles, evaluación y puntuación;
- separación entre puntuación y afinidades;
- trazabilidad de razones a dominios, perfiles, fuentes y límites;
- autorización negativa y no exposición de datos;
- accesibilidad con personas y herramientas pertinentes;
- errores, interrupciones, reanudación y datos faltantes;
- migraciones, recuperación y retención, si se adoptan;
- contrato backend/frontend y compatibilidad de versiones;
- análisis que no escriba automáticamente en producción.

No existen resultados verdes, datos de prueba, conteos, infraestructura ni capacidad operativa que reportar hoy. La evidencia deberá incluir comando o procedimiento real, versión, fecha, salida y límites cuando una fase futura lo verifique.

## 10. Secuenciación futura sin duplicar el plan

El reparto provisional de personas y traspasos está en [06 — Reparto de implementación por fases](./06-reparto-de-implementacion-por-fases.md). Este documento no duplica ese plan ni lo convierte en cronograma.

La secuencia candidata es:

1. cerrar puertas de investigación y autorización institucional;
2. decidir el cambio cruzado y sus límites por repositorio;
3. acordar el contrato de dominio/API en `psicotest-backend`;
4. revisar el consumo y la accesibilidad en `psicotest-frontend`;
5. implementar solo el alcance autorizado, con OpenSpec propio en cada repositorio;
6. verificar cada repositorio y el contrato cruzado antes de considerar la entrega.

Ninguna etapa avanza automáticamente por completar la anterior. Si falta evidencia de catálogo, población, respuesta-proceso, privacidad o validez, se bloquea la implementación y se registra la decisión necesaria.

## Decisiones técnicas pendientes

| Decisión | Riesgo de decidir demasiado pronto | Estado |
| --- | --- | --- |
| Marco de trabajo de frontend | Puede fijar modalidad y accesibilidad antes de conocer usuarios y dispositivos. | Pendiente. |
| Lenguaje y marco de trabajo de backend | Puede limitar análisis, mantenimiento y capacidades institucionales. | Pendiente. |
| Base y almacenamiento | Puede sobrerrecolectar o dificultar retención y eliminación. | Pendiente. |
| Contrato de catálogo | Puede perpetuar duplicados o estados sin autoridad. | Pendiente de [S29][S30] y reconciliación institucional. |
| Constructos y puntuación | Puede convertir hipótesis en autoridad. | Pendiente de investigación psicométrica. |
| Forma del resultado | Puede producir una única respuesta engañosa. | Mantener pluralidad y exploración; detalle pendiente. |
| Identidad y permisos | Puede inventar roles o capacidades profesionales. | Pendiente de gobernanza. |
| OpenSpec y Engram | Puede mezclar artefactos o usar memoria como privacidad. | OpenSpec futuro por repositorio; memorias externas ya separadas en Engram; identidad local futura pendiente. |
| Entrega cruzada | Puede desincronizar frontend y backend. | ID cruzado, enlaces recíprocos y contrato backend pendiente. |
| Operación y despliegue | Puede crear una capacidad no soportada institucionalmente. | Pendiente de necesidades y recursos reales. |

**Resultado de esta etapa:** hay una arquitectura candidata y reglas de coordinación, no una aplicación, una API, una pila tecnológica seleccionada ni una autorización de implementación.
