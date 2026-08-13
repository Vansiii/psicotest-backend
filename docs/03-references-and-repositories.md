# Referencias, fuentes de evidencia e inspiración para repositorios

**Decisión primero:** las normas y guías profesionales son restricciones principales; la investigación y los recursos educativos son contexto; los repositorios de software son inspiración arquitectónica. Ninguna fuente de esta lista valida por sí sola un instrumento, una puntuación, un perfil de programa o una recomendación de TestPsico. Ningún repositorio es una dependencia aprobada.

Los IDs son citas estables para los demás documentos. Las fuentes [S1]–[S27] corresponden a la revisión inicial consultada el **2026-08-04**. Las fuentes [S28]–[S38] fueron verificadas o consultadas el **2026-08-12**; sus fechas, alcance y vigencia deben revisarse antes de una decisión institucional, legal o técnica importante.

## Mapa de fuentes

| Categoría | IDs | Papel |
| --- | --- | --- |
| Normativa y orientación profesional internacional | [S1]–[S8] | Validez, confiabilidad, equidad, ética, usuarios calificados, privacidad, administración y reporte. |
| Contexto ocupacional y tecnológico | [S9]–[S10] | Vocabulario para analizar actividades y contextos; no evidencia individual. |
| Recursos educativos y técnicos | [S11]–[S12] | Aprendizaje y planificación de análisis psicométricos; no sustituyen la validación de uso. |
| Investigación y contexto conceptual | [S13]–[S16] | Hipótesis sobre análisis de trabajo, capacidades y personalidad; no predicciones deterministas. |
| Contexto institucional UAGRM | [S22]–[S23], [S28]–[S31] | Orientación institucional, estatuto, oferta pública y estudio local; no validación de TestPsico. |
| Contexto legal, inclusión y adaptación | [S24]–[S27] | Privacidad, educación inclusiva, accesibilidad y adaptación lingüística/cultural. |
| Inspiración de repositorios | [S17]–[S21] | Patrones de arquitectura y flujo; no aprobación de código o dependencia. |
| Documentación futura y continuidad contextual | [S32]–[S38] | OpenSpec por repositorio, guía portátil `AGENTS.md` y memorias de investigación separadas en Engram. |

## Límite entre autoridad e inspiración

Una fuente es **autoridad contextual o normativa** cuando se usa para justificar una restricción, una pregunta de gobernanza, una descripción institucional o un criterio de investigación, siempre dentro de su alcance y fecha. Una fuente es **inspiración** cuando ayuda a formular arquitectura, vocabulario o un flujo de trabajo, pero no autoriza una dependencia, una interpretación psicométrica, un dato de catálogo o una práctica de privacidad.

La documentación institucional de UAGRM debe prevalecer para el catálogo y sus versiones. OpenSpec, Git y los documentos del proyecto deben prevalecer para el comportamiento y los cambios de software. Engram solo aporta continuidad contextual y nunca es la fuente normativa única. Los repositorios externos requieren revisión independiente de licencia, mantenimiento, seguridad, accesibilidad, exactitud y ajuste al propósito.

## Normativa y orientación profesional internacional

### [S1] AERA/APA/NCME — *Standards for Educational and Psychological Testing* (2014)

- **URL:** [Archivos de acceso abierto](https://www.testingstandards.net/open-access-files.html)
- **Por qué importa:** Marco central para validez, confiabilidad, precisión/error, equidad, diseño, puntuaciones, escalas, normas, cortes, administración, reporte, documentación y derechos.
- **Uso en TestPsico:** Organizar el argumento de validez y las puertas de investigación. No valida un uso no especificado ni proporciona cortes de TestPsico.

### [S2] APA — resumen de estándares de evaluación

- **URL:** [Resumen oficial de APA](https://www.apa.org/science/programs/testing/standards)
- **Por qué importa:** Punto de entrada oficial a los estándares y su papel en la práctica.
- **Uso en TestPsico:** Orientación y verificación cruzada de [S1]; las afirmaciones detalladas deben citar [S1].

### [S3] SIOP — *Principles for the Validation and Use of Personnel Selection Procedures*, quinta edición (2018)

- **URL:** [PDF oficial](https://www.apa.org/ed/accreditation/personnel-selection-procedures.pdf)
- **Por qué importa:** Vincula la validación con la interpretación propuesta y la inferencia relacionada con el trabajo, y exige múltiples fuentes de evidencia.
- **Uso en TestPsico:** Sirve para comprender por qué KSAO y la evidencia ocupacional no autorizan selección automática. El uso laboral permanece fuera del alcance.

### [S4] International Test Commission — *Guidelines on Test Use*

- **URL:** [PDF de la guía](https://www.intestcom.org/files/guideline_test_use.pdf)
- **Por qué importa:** Trata usuarios calificados, responsabilidad ética, poblaciones pertinentes, confiabilidad, validez, sesgo, equidad, confidencialidad, administración, interpretación y retroalimentación.
- **Uso en TestPsico:** Define límites de uso responsable y competencias para una etapa futura.

### [S5] International Test Commission — *Guidelines on Computer-Based and Internet Delivered Testing*

- **URL:** [PDF de la guía](https://www.intestcom.org/files/guideline_computer_based_testing.pdf)
- **Por qué importa:** Aborda modalidades abiertas, supervisadas y administradas, identidad, seguridad, efectos tecnológicos y protección de participantes.
- **Uso en TestPsico:** Consultar antes de elegir modalidad o asumir equivalencia entre administración presencial y digital.

### [S6] ITC/ATP — *Guidelines for Technology-Based Assessment*, versión 1.1 (julio de 2025)

- **URL:** [PDF de la guía](https://www.intestcom.org/upload/media-library/tba-guidelines-ver-11-july-2025-1754044782Z3vV9.pdf)
- **Por qué importa:** Cubre validez digital, equidad, accesibilidad, seguridad, privacidad, varianza irrelevante por interfaz y adaptación global.
- **Uso en TestPsico:** Lista de riesgos tecnológicos. La interfaz forma parte de las condiciones de evaluación.

### [S7] APA — *Guidelines for Psychological Assessment and Evaluation*

- **URL:** [PDF de las guías](https://www.apa.org/about/policy/guidelines-psychological-assessment-evaluation.pdf)
- **Por qué importa:** Trata competencia, instrumentos estandarizados, constructos, procedimientos, interpretación, diversidad y cuidado en usos de alto impacto.
- **Uso en TestPsico:** Límites profesionales y de reporte. No convierte el proyecto en clínico ni autoriza diagnóstico.

### [S8] APA — *Ethical Principles of Psychologists and Code of Conduct* (2017), especialmente la sección 9

- **URL:** [Código de ética](https://www.apa.org/ethics/code/ethics-code-2017.pdf)
- **Por qué importa:** Trata fundamentos del uso de evaluaciones, consentimiento, datos, construcción, interpretación, usuarios calificados, explicación de resultados y seguridad del test.
- **Uso en TestPsico:** Referencia ética para consentimiento, privacidad, acceso, reporte y seguridad. Se deben aplicar también la legislación, las reglas institucionales y los requisitos profesionales pertinentes.

## Contexto ocupacional y tecnológico

### [S9] U.S. Department of Labor — modelo de contenido O*NET

- **URL:** [Content Model](https://www.onetcenter.org/content.html)
- **Por qué importa:** Ofrece vocabulario de características, habilidades, capacidades, estilos de trabajo, conocimiento, actividades y contexto laboral.
- **Uso en TestPsico:** Organizar preguntas sobre actividades y contextos cuando sean pertinentes. No es diagnóstico ni predicción individual, y no es un requisito de orientación educativa.

### [S10] U.S. Department of Labor — documentación de la base O*NET

- **URL:** [Diccionario de la base](https://www.onetcenter.org/dl_files/database/db_30_0_dictionary.pdf)
- **Por qué importa:** Explica campos del modelo de contenido y ayuda a distinguir evidencia ocupacional de medición individual.
- **Uso en TestPsico:** Referencia para taxonomías, conservando contexto de origen. No reemplaza un análisis local ni valida perfiles UAGRM.

## Recursos educativos y técnicos

### [S11] NCME/ETS Digital Module 08 — *Foundations of Operational Item Analysis*

- **URL:** [Descripción general en PDF](https://ncme.org/wp-content/uploads/2025/10/Foundations-of-Operational-Item-Analysis-Overview.pdf)
- **Por qué importa:** Introduce el análisis de ítems con CTT e IRT, dificultad, discriminación, distractores, tamaño muestral, datos faltantes, sesgo de ítems e interpretación.
- **Uso y límite en TestPsico:** Usar solo con fines educativos y contextuales para planificar análisis de pilotos y formular preguntas sobre el comportamiento de los ítems. Las estadísticas de ítems no sustituyen la definición del constructo, el análisis de equidad ni la validación específica del uso; no permiten interpretar puntuaciones automáticamente, predecir determinísticamente a individuos, justificar contratación ni validar TestPsico.

### [S12] Anna Brown — *Psychometrics in Exercises using R and RStudio*

- **URL:** [Recurso educativo gratuito](https://bookdown.org/annabrown/psychometricsR/)
- **Por qué importa:** Ofrece una progresión estructurada por escalamiento, CTT/confiabilidad, modelos factoriales, EFA/CFA, IRT, DIF e invariancia longitudinal o entre grupos.
- **Uso y límite en TestPsico:** Usar solo con fines educativos y contextuales para aprendizaje y ejercicios de análisis reproducible. Los ejemplos son educativos: los modelos y decisiones deben elegirse para el constructo y la población de TestPsico, no copiarse mecánicamente; no permiten interpretar puntuaciones automáticamente, predecir determinísticamente a individuos, justificar contratación ni validar TestPsico.

## Investigación y contexto conceptual

### [S13] Peterson et al./O*NET — antecedentes y análisis del trabajo

- **URL:** [Capítulo de National Academies](https://www.nationalacademies.org/read/12814/chapter/5)
- **Por qué importa:** Aporta antecedentes sobre O*NET y la razón de ser de las taxonomías y del análisis del trabajo.
- **Uso y límite en TestPsico:** Usar solo con fines educativos y contextuales para respaldar el análisis de las demandas del trabajo antes de seleccionar medidas individuales. Es evidencia de antecedentes, no un estudio de validación de TestPsico; no permite interpretar puntuaciones automáticamente, predecir determinísticamente a individuos ni autoriza uso en contratación.

### [S14] Panorama de CHC

- **URL:** [Artículo de acceso abierto en PDF](https://mdpi-res.com/d_attachment/jintelligence/jintelligence-11-00032/article_deploy/jintelligence-11-00032-v2.pdf?version=1676015614)
- **Por qué importa:** Ofrece una taxonomía candidata de capacidades cognitivas y una forma de analizar constructos amplios y específicos.
- **Uso y límite en TestPsico:** Usar solo con fines educativos y contextuales como taxonomía conceptual para investigar; no permite interpretar puntuaciones automáticamente, inferir la capacidad de una persona a partir de una etiqueta ni predecir determinísticamente a individuos; tampoco autoriza el uso en contratación ni valida TestPsico.

### [S15] Evidencia sobre responsabilidad laboral

- **URL:** [Artículo en PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6859351/)
- **Por qué importa:** Aporta evidencia contextual para analizar la responsabilidad y sus resultados ocupacionales.
- **Uso y límite en TestPsico:** Usar solo con fines educativos y contextuales para formular hipótesis cautelosas. Toda asociación debe reexaminarse para la población, el criterio, el contexto, el método de medición y el uso previsto; no permite interpretar puntuaciones automáticamente, predecir determinísticamente a individuos, justificar contratación ni validar TestPsico.

### [S16] Personalidad en contextos de alto impacto, falseamiento y evidencia predictiva en postulantes

- **URL:** [Artículo vinculado al DOI](https://doi.org/10.1111/ijsa.12413)
- **Por qué importa:** Sustenta la cautela ante la evaluación de personalidad en contextos de alto impacto, la distorsión o el falseamiento de respuestas y la evidencia predictiva limitada en postulantes reales.
- **Uso y límite en TestPsico:** Usar solo con fines educativos y contextuales para rechazar afirmaciones deterministas de personalidad para contratación y exigir un diseño de validación específico antes de considerar cualquier uso con consecuencias. No permite interpretar puntuaciones automáticamente, predecir determinísticamente a individuos ni validar TestPsico.

## Inspiración de repositorios de código abierto

Estos repositorios son referencias de arquitectura, no una aprobación de uso en producción. Antes de reutilizar código se deben revisar licencia vigente, dependencias, seguridad, accesibilidad, mantenimiento, exactitud y ajuste al propósito.

### [S17] `psychTestR`

- **URL:** [Repositorio GitHub](https://github.com/pmcharrison/psychTestR)
- **Propósito:** Paquete de R para interfaces de experimentos conductuales.
- **Lecciones:** Separación de líneas de tiempo, módulos, resultados, administración y pruebas.
- **Licencia:** GPL-3.0, confirmada por el README del repositorio en la revisión inicial.
- **Precauciones:** Compatibilidad de licencia, mantenimiento, seguridad, privacidad y adecuación psicométrica deben revisarse antes de cualquier uso.

### [S18] `psychTestRCAT`

- **URL:** [Repositorio GitHub](https://github.com/pmcharrison/psychTestRCAT)
- **Propósito:** Paquete de R para tests adaptativos de capacidad basados en `IRT`.
- **Lecciones:** Representación de bancos de ítems, lógica adaptativa y reglas de detención.
- **Licencia:** No confirmada en la revisión inicial.
- **Precauciones:** No compensa constructos indefinidos ni datos insuficientes; se deben revisar calibración, supuestos, equidad, seguridad y mantenimiento.

### [S19] `jsPsych`

- **URL:** [Repositorio GitHub](https://github.com/jspsych/jsPsych)
- **Propósito:** Marco de trabajo JavaScript para experimentos conductuales en navegador.
- **Lecciones:** Arquitectura de plugins y líneas de tiempo, datos por evento y separación de tareas.
- **Licencia y versión:** Confirmar en el repositorio actual antes de decidir.
- **Precauciones:** Compatibilidad, minimización de datos, seguridad, accesibilidad, fidelidad temporal y varianza irrelevante al constructo.

### [S20] `lib-psychometrics` de Learnosity

- **URL:** [Repositorio GitHub](https://github.com/Learnosity/lib-psychometrics)
- **Propósito:** Biblioteca Java de psicometría.
- **Lecciones:** Separación de `CTT`, `IRT`, análisis factorial, `DIF`, confiabilidad, `SEM`, vinculación y equiparación.
- **Licencia:** Apache-2.0, confirmada por el README en la revisión inicial.
- **Precauciones:** La licencia permisiva no demuestra corrección numérica, validez estadística, ajuste de API ni mantenimiento.

### [S21] `IRTC`

- **URL:** [Repositorio GitHub](https://github.com/weiandata/IRTC)
- **Propósito:** Ejemplo de paquete o flujo de trabajo de `IRT` en R.
- **Lecciones:** Limpieza, puntuación, estimación, ajuste de ítems y reporte reproducible.
- **Licencia y mantenimiento:** No confirmados en la revisión inicial.
- **Precauciones:** Revisar supuestos, datos faltantes, reproducibilidad, versiones y ajuste a la población.

## Contexto institucional oficial de UAGRM

### [S22] Departamento de Orientación Vocacional de UAGRM — URL institucional histórica

- **URL:** [Página institucional](https://www.uagrm.edu.bo/index.php/unidades-administrativas/orientacin-vocacional)
- **Por qué importa:** Describe acompañamiento vocacional, educativo y psicopedagógico, intereses, capacidades, rendimiento, permanencia y contexto de “Test Psicotécnico”.
- **Uso y límite:** Evidencia de un contexto institucional y de posibles interlocutores. No valida ítems, puntuaciones, normas ni interpretaciones de TestPsico.

### [S23] UAGRM — *Estatuto UAGRM 2024 vigente* (RR 061/2024)

- **URL:** [PDF oficial](https://files.uagrm.edu.bo/entidad/140/file/2026/documentos/EstatutoUAGRM_2024_Vigente_RR_061-2024.pdf)
- **Por qué importa:** Aporta contexto institucional sobre autonomía, cogobierno, igualdad, no discriminación y misión educativa.
- **Uso en TestPsico:** Identificar gobernanza, inclusión y revisiones institucionales. No valida una medida ni autoriza un uso.

### [S28] UAGRM — Orientación Vocacional, página oficial vigente consultada

- **URL:** [Orientación Vocacional](https://www.uagrm.edu.bo/unidades-administrativas/orientacin-vocacional)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Describe apoyo personalizado para elegir o reconsiderar carreras, autoconocimiento, intereses, capacidades, contexto socioeconómico, rendimiento/permanencia y un “Test Psicotécnico”.
- **Uso y límite:** Prueba contexto institucional y una posible necesidad de descubrimiento con Orientación Vocacional. No prueba que exista un instrumento TestPsico válido ni aporta ítems, puntuaciones, baremos o evidencia de uso.

### [S29] UAGRM — página oficial de admisiones y niveles

- **URL:** [Admisiones y niveles](https://www.uagrm.edu.bo/admisiones/niveles)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Informa 18 facultades y 69 programas de formación profesional en Santa Cruz de la Sierra.
- **Límites:** No necesariamente representa el catálogo universitario completo y no ofrece metadatos confiables de versión, vigencia o identificadores estables. No se debe usar el número como catálogo final.
- **Uso en TestPsico:** Fuente contextual para reconciliación, no autoridad suficiente para publicar recomendaciones sin una versión institucional autorizada.

### [S30] UAGRM — página oficial de carreras

- **URL:** [Carreras](https://www.uagrm.edu.bo/carreras)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Expone aproximadamente 80 entradas o páginas, incluidas repeticiones por facultad o sitio y campos de texto desiguales.
- **Límites:** No constituye un catálogo versionado confiable; la cantidad aproximada no debe elegirse frente a la cifra de [S29].
- **Uso en TestPsico:** Evidencia de la necesidad de reconciliar fuentes, duplicados, IDs, estado, sitio, modalidad, disponibilidad y fechas antes de recomendar.

### [S31] UAGRM — estudio local sobre postulantes de Ciencias Económicas y Empresariales

- **URL:** [Artículo en la Revista Científica UAGRM](https://ojs.uagrm.edu.bo/revista-cientifica-uagrm/article/view/10)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Estudio descriptivo, transversal y no experimental de 122 postulantes de esa facultad en marzo de 2023; examina dimensiones personales, familiares y socioeconómicas y reporta predominio de factores familiares y socioeconómicos.
- **Límites:** No demuestra causalidad, no representa toda la UAGRM y no justifica pesos universales, normas ni recomendaciones individuales.
- **Uso en TestPsico:** Fuente de contexto e hipótesis para muestreo y respuesta-proceso; requiere replicación y evidencia específica para cualquier interpretación.

## Contexto legal, inclusión y adaptación

### [S24] AGETIC — *Manual de Protección de Datos* (junio de 2025)

- **URL:** [PDF oficial](https://agetic.gob.bo/sites/default/files/2025-06/Manual-de-Proteccion-de-Datos-2-firmado.pdf)
- **Por qué importa:** Describe fundamentos constitucionales y principios de finalidad, proporcionalidad, confidencialidad, seguridad, transparencia, responsabilidad y derechos tipo ARCO.
- **Límite:** También presenta un anteproyecto o marco propuesto; no es asesoría legal ni prueba de una ley integral vigente.
- **Uso en TestPsico:** Insumo para minimización, consentimiento, acceso, retención y solicitudes, sujeto a revisión institucional y legal.

### [S25] Bolivia — Ley de Educación 070

- **URL:** [PDF de contexto legal](https://sea.gob.bo/digesto/CompendioII/D/28_L_70.pdf)
- **Por qué importa:** Contexto nacional para educación superior, inclusión y pertinencia cultural.
- **Uso y límite:** Formula preguntas de revisión institucional y legal; no valida medidas ni autoriza admisión, contratación, clínica o normas nacionales.

### [S26] Página de alianza de Naciones Unidas — *Universal Accessibility in Bolivian Higher Education: Training and Counselling within UAGRM*

- **URL:** [Página de alianza](https://sdgs.un.org/partnerships/universal-accessibility-bolivian-higher-education-training-and-counselling-within)
- **Por qué importa:** Documenta un proyecto de accesibilidad y educación inclusiva en UAGRM con diagnóstico de barreras, revisión experta, pilotaje y una escala local validada.
- **Uso y límite:** Justifica trabajo explícito de accesibilidad, barreras y validación local; no es una matriz psicométrica ni valida TestPsico.

### [S27] International Test Commission — *Guidelines for Translating and Adapting Tests*, segunda edición, versión 2.4 (2017)

- **URL:** [PDF de la guía](https://www.intestcom.org/files/guideline_test_adaptation_2ed.pdf)
- **Por qué importa:** Orienta traducción, adaptación cultural, documentación, revisión y evidencia al mover un test entre lenguas o contextos.
- **Uso en TestPsico:** Guía para adaptación en español y futuras poblaciones bolivianas. No proporciona ítems, normas, puntuaciones ni validez del proyecto.

## OpenSpec y guía portátil para el futuro; Engram para la continuidad actual

### [S32] OpenSpec — conceptos centrales

- **URL:** [Core concepts](https://openspec.dev/docs/core-concepts)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Define `openspec/specs/` como comportamiento acordado vigente y `openspec/changes/<name>/` como trabajo propuesto en Markdown.
- **Uso en TestPsico:** Cada repositorio futuro tendrá su propio `openspec/`; las especificaciones y cambios serán parte del registro normativo de ese repositorio. No se inicializa nada ahora.

### [S33] OpenSpec — revisión de cambios

- **URL:** [Reviewing changes](https://openspec.dev/docs/reviewing-changes)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Describe el flujo de propuesta, deltas de especificación, diseño, tareas y revisión.
- **Uso en TestPsico:** Guiar cambios futuros dentro de cada repositorio, después de que investigación y alcance autoricen implementación. No se debe asumir que un artefacto existe hoy.

### [S34] OpenSpec — stores

- **URL:** [Stores](https://openspec.dev/docs/stores)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Documenta la opción beta de Stores y sus diferencias con el uso normal dentro de un repositorio.
- **Decisión:** No usar la beta independiente de Stores como línea base. TestPsico tendrá un `openspec/` independiente dentro de `psicotest-frontend` y otro dentro de `psicotest-backend`, cuando corresponda; no se inicializan ahora.

### [S35] `AGENTS.md` — guía abierta para agentes

- **URL:** [agents.md](https://agents.md/)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Propone un README abierto y simple, normalmente en la raíz, con propósito, configuración, construcción, pruebas, seguridad y contribución.
- **Uso en TestPsico:** Cada repositorio futuro tendrá una guía compacta y portable para agentes sin Gentle AI. No será una copia del ecosistema ni contendrá personas, instrucciones, registros de revisión o comandos propietarios.

### [S36] Engram — configuración y preparación de agentes

- **URL:** [AGENT-SETUP.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/AGENT-SETUP.md)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Describe el uso con agentes compatibles con MCP y la configuración explícita en la raíz del repositorio para una identidad de proyecto determinista.
- **Uso en TestPsico:** Ya se usan memorias de investigación curadas y separadas para los proyectos `psicotest-frontend` y `psicotest-backend`, incluida la decisión de alcance de toda la UAGRM. La identidad determinista futura dentro de cada repositorio, mediante `.engram/config.json` y un nombre explícito, sigue pendiente; no se ha creado ningún archivo local. Las memorias no contendrán credenciales, respuestas brutas, datos identificables ni contenido psicométrico no aprobado.

### [S37] Engram — arquitectura

- **URL:** [ARCHITECTURE.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/ARCHITECTURE.md)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Explica almacenamiento, recuperación progresiva y la diferencia entre memorias de proyecto y personales.
- **Límites y política local:** `scope: project` es una convención semántica de búsqueda, no una frontera de privacidad; la sincronización puede exportar observaciones de proyecto y personales. Engram no debe guardar datos de participantes ni reemplazar OpenSpec, Git o la documentación.

### [S38] Engram — uso en equipos

- **URL:** [TEAM-USAGE.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/TEAM-USAGE.md)
- **Fecha de consulta:** 2026-08-12.
- **Por qué importa:** Describe memorias estructuradas y curadas para decisiones y descubrimientos compartidos.
- **Uso en TestPsico:** Mantener una convención de temas común entre repositorios, con las memorias de investigación ya separadas por proyecto y enlaces al cambio cruzado. Si Engram no está disponible, continuar desde `AGENTS.md`, OpenSpec y la documentación del repositorio, informando la capacidad faltante.

## Matriz de inspiración y decisión de dependencia

| Fuente | Inspiración segura | Decisión de dependencia | Revisión bloqueante |
| --- | --- | --- | --- |
| [S17]–[S21] repositorios | Modularidad, líneas de tiempo, datos y análisis reproducible | No aprobada | Licencia, mantenimiento, seguridad, privacidad, accesibilidad, exactitud y ajuste. |
| [S1]–[S16] guías y estudios | Requisitos, vocabulario, hipótesis y listas de revisión | Nunca dependencia de ejecución | Interpretación, jurisdicción, población y uso. |
| [S22]–[S31] UAGRM y contexto local | Partes interesadas, catálogo, gobernanza, accesibilidad y preguntas de muestreo | Nunca sustituto del catálogo o validación | Fuente autorizada, versión, alcance, revisión institucional y límites de generalización. |
| [S32]–[S34] OpenSpec | Artefactos de cambio por repositorio y comportamiento acordado | Una instalación futura por repositorio | Alcance del repositorio, decisión de implementación y revisión de cambios. |
| [S35] `AGENTS.md` | Descubrimiento portátil y reglas del proyecto | Un archivo futuro por repositorio | Propósito, seguridad, lectura, pruebas reales y reporte de bloqueos. |
| [S36]–[S38] Engram | Memorias de investigación curadas y separadas por proyecto, con enlaces entre repositorios | Memorias externas ya existentes; identidad local futura por repositorio | No guardar datos sensibles; si no está disponible, aplicar degradación explícita. |

**Regla:** la inspiración puede orientar preguntas y arquitectura; una dependencia o una afirmación institucional cambia la superficie legal, operativa, psicométrica o de mantenimiento y exige una decisión documentada.
