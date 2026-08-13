# Plan de investigación: del catálogo completo a la orientación responsable

**Decisión primero:** TestPsico es una iniciativa de investigación. Ninguna fase de implementación ha comenzado. El propósito propuesto es ofrecer orientación vocacional/educativa de bajo riesgo para carreras y programas de toda la UAGRM a estudiantes de secundaria, postulantes y otras personas interesadas, sin afirmar admisión, elegibilidad, éxito académico, empleabilidad, diagnóstico clínico ni una “carrera correcta”.

La cobertura y la recolección pueden organizarse gradualmente por facultad, campus/sitio, nivel, modalidad o disponibilidad para hacer viable la investigación. Esa organización es una estrategia de cobertura y muestreo; **no** es un pre-filtro obligatorio de la recomendación.

El catálogo institucional y la evidencia psicométrica son líneas separadas. El primero determina qué programas autorizados pueden aparecer; la segunda estudia qué significan las respuestas; la evidencia de interpretación y uso estudia si una salida plural se entiende y sirve para explorar.

## Estado de implementación

| Elemento | Estado |
| --- | --- |
| `psicotest-frontend` | Repositorio independiente vacío, sin fase iniciada. |
| `psicotest-backend` | Repositorio independiente vacío, sin fase iniciada. |
| OpenSpec | Se planifica un `openspec/` propio por repositorio en el futuro; no se ha inicializado. |
| Engram | Ya se usan memorias de investigación curadas, separadas para `psicotest-frontend` y `psicotest-backend`, incluida la decisión de alcance de toda la UAGRM. No se ha creado `.engram/config.json` ni otro archivo local; la identidad determinista futura por repositorio queda pendiente. No es almacén normativo ni de datos de participantes. |
| `AGENTS.md` | Se planifica una guía raíz compacta y portable por repositorio; no se ha creado. |
| Fases de implementación | No iniciadas y condicionadas a las puertas de investigación de este documento. |

## Ruta general

| Etapa | Pregunta principal | Evidencia o salida requerida | Puerta de salida |
| --- | --- | --- | --- |
| 0. Límites y gobierno | ¿Qué puede afirmar TestPsico sin adquirir autoridad indebida? | Propósito, usos prohibidos, poblaciones, riesgos, privacidad y responsables | Propósito de bajo riesgo aprobado para investigación. |
| 1. Marco UAGRM y partes interesadas | ¿A quiénes se quiere incluir y quién gobierna el trabajo? | Mapa de responsables, población, sitios, niveles, modalidades, accesibilidad y revisión institucional | Marco muestral y ruta de aprobación definidos. |
| 2. Reconciliación del catálogo | ¿Cuál es la oferta autorizada y vigente de toda la UAGRM? | Catálogo con IDs estables, fuentes, versiones, estado, fechas y responsables | Ninguna recomendación usa una fuente no reconciliada. |
| 3. Muestreo y respuesta-proceso | ¿Las personas previstas entienden el propósito, preguntas y límites? | Plan de muestreo, comprensión, entrevistas, accesibilidad y salvaguardas para menores | Barreras críticas corregidas o limitadas. |
| 4. Perfiles y matriz de especificación | ¿Qué se compara y con qué evidencia? | `program_profile`, constructos, intereses, preferencias, contenido original y reglas de incertidumbre | Trazabilidad completa sin criterios ocultos de selección. |
| 5. Piloto exploratorio | ¿La salida plural es comprensible y útil para explorar? | Datos y condiciones del piloto, afinidades, razones, faltantes y utilidad | Uso permanece bajo riesgo y los límites son visibles. |
| 6. Validez, equidad y generalización | ¿La interpretación aplica a las poblaciones declaradas? | Precisión, estructura, respuesta-proceso, equidad, accesibilidad, consecuencias y réplica | Afirmaciones acotadas al contexto respaldado. |
| 7. Candidato de operación | ¿Puede existir un prototipo sin exceder la evidencia? | Gobierno de datos, controles, reporte, monitoreo, pausa y documentación | Autorización explícita para planificar implementación. |
| 8. Implementación futura | ¿Qué software puede construirse bajo las puertas aprobadas? | Cambio específico por repositorio, contratos, pruebas y entregas | Nueva decisión; nunca comienza automáticamente por completar una etapa de investigación. |

## Pregunta central

La primera pregunta no es “¿qué carrera es la correcta?”, sino:

> ¿Puede TestPsico ofrecer una exploración comprensible, plural y útil de programas autorizados de toda la UAGRM, con evidencia institucional y psicométrica separadas, sin convertir la afinidad en una decisión?

## Etapa 0 — Límites y gobierno

### Decidir

- propósito de orientación vocacional/educativa exploratoria y de bajo riesgo;
- poblaciones previstas: secundaria, postulantes y otras personas interesadas;
- idioma, contexto cultural, modalidad, acceso y acomodaciones;
- responsables de Orientación Vocacional, facultades, programas, accesibilidad, ética/investigación, registros, tecnología y privacidad;
- consentimiento, asentimiento cuando corresponda, retiro, minimización, acceso, retención, eliminación y atención de solicitudes;
- usos permitidos y usos prohibidos;
- consecuencias de una afinidad mal interpretada;
- jurisdicción y requisitos institucionales o legales aplicables.

La página oficial de Orientación Vocacional de UAGRM demuestra contexto institucional, no validez del instrumento [S28]. Las decisiones deben quedar aprobadas por responsables competentes, no inferirse de la existencia de la página.

### Producir

- declaración de propósito y uso;
- registro de riesgos, daños posibles y mitigaciones;
- mapa de datos y retención;
- registro de responsables y escalamiento;
- lenguaje visible que excluya diagnóstico, admisión, elegibilidad, éxito, empleabilidad y decisiones de alto impacto;
- protocolo específico para participantes menores o jóvenes, con revisión de comprensión, consentimiento/asentimiento y acompañamiento.

### Puerta 0

- [ ] Propósito, población, nivel de consecuencias y límites están escritos.
- [ ] Uso de bajo riesgo y usos prohibidos fueron aprobados.
- [ ] Privacidad, acceso, retención, eliminación y ruta de revisión están definidos antes de recolectar datos.
- [ ] No existe un ranking, corte o etiqueta definitiva como requisito oculto.

## Etapa 1 — Marco UAGRM, población y partes interesadas

### Trabajo

1. Identificar interlocutores institucionales y responsabilidades de decisión.
2. Definir el marco de población: estudiantes de secundaria, postulantes, personas interesadas y participantes de investigación, sin suponer que son intercambiables.
3. Describir facultades, campus/sitios, niveles, modalidades, disponibilidad, idioma, acceso y posibles subgrupos.
4. Diseñar muestreo representativo o, si el piloto es intencional, declarar qué generalizaciones quedan excluidas.
5. Prever respuesta-proceso y accesibilidad para jóvenes, menores, personas con discapacidad, distintos dispositivos y condiciones de conectividad.
6. Registrar cómo se gestionan consentimiento/asentimiento, retiro, preguntas, correcciones y derivación a orientación.

La cobertura por facultad o sitio puede ser escalonada. Ninguna etapa escalonada autoriza a excluir permanentemente programas de otra facultad de la recomendación si el propósito declarado es toda la UAGRM.

### Producir

- mapa de partes interesadas y responsabilidades;
- marco muestral y plan de cobertura;
- protocolo de reclutamiento y salvaguardas;
- plan de adaptación lingüística y cultural;
- plan de accesibilidad, acomodaciones y respuesta-proceso;
- registro de supuestos, exclusiones y límites.

### Puerta 1

- [ ] La población prevista y las condiciones de inclusión están definidas.
- [ ] El muestreo distingue cobertura de recomendación.
- [ ] Hay ruta institucional, ética/investigación y de privacidad.
- [ ] Las salvaguardas para menores y jóvenes fueron revisadas cuando correspondan.
- [ ] La generalización prevista es proporcional a la muestra.

## Etapa 2 — Reconciliación del catálogo institucional

### Evidencia inicial

- Admisiones informa 18 facultades y 69 programas en Santa Cruz de la Sierra [S29].
- La página de carreras expone aproximadamente 80 entradas o páginas, con repeticiones por facultad o sitio y campos libres desiguales [S30].

Estas cifras tienen alcances distintos. No se debe elegir una como número oficial ni presentar la página pública como catálogo versionado.

### Trabajo

1. Obtener una fuente institucional autorizada y nombrar a su responsable.
2. Reconciliar nombres, alias, duplicados, facultad, sitio, nivel, modalidad y disponibilidad.
3. Asignar identificadores estables y separar ID oficial de cualquier ID interno futuro.
4. Registrar versión, fecha de consulta, fecha de vigencia/efectividad, estado, fuente y método de reconciliación.
5. Documentar programas ausentes, repetidos, discontinuados o con datos contradictorios.
6. Definir cómo se revisan cambios del catálogo y qué ocurre con resultados históricos.
7. Mantener la lista completa autorizada, aunque la recolección o la revisión de perfiles se despliegue por etapas.

### Producir

- catálogo reconciliado de alcance UAGRM;
- matriz de fuentes y discrepancias;
- registro de versiones y fechas;
- diccionario de metadatos;
- reglas para publicación, suspensión y cambios;
- lista de programas que no pueden aparecer hasta resolver evidencia.

### Puerta 2

- [ ] El catálogo tiene autoridad institucional identificable.
- [ ] Cada programa autorizado tiene ID estable, estado y versión.
- [ ] Facultad, sitio, nivel, modalidad y disponibilidad son metadatos documentados.
- [ ] Las discrepancias entre [S29] y [S30] están registradas, no ocultas.
- [ ] No se publica ninguna recomendación desde una lista sin reconciliar.

## Etapa 3 — Muestreo, respuesta-proceso y accesibilidad

### Trabajo

- preespecificar preguntas de comprensión, utilidad, interpretación y límites;
- entrevistar o probar con las poblaciones definidas, incluyendo jóvenes cuando corresponda;
- estudiar consentimiento/asentimiento, comprensión del propósito y posibilidad de retiro;
- probar lenguaje, lectura, teclado, dispositivos, lectores de pantalla, contraste, tiempo, conectividad y acomodaciones;
- registrar estrategias inesperadas, presión social, interrupciones, faltantes y errores técnicos;
- evaluar si las personas interpretan la salida como exploración y no como admisión, diagnóstico o pronóstico;
- controlar diferencias entre modalidades solo cuando exista una pregunta explícita de equivalencia.

El estudio local de 122 postulantes de Ciencias Económicas y Empresariales [S31] puede ayudar a formular hipótesis de contexto y muestreo, pero no sustituye una muestra de toda la población ni permite transferir pesos a todas las carreras.

### Producir

- informe de respuesta-proceso y comprensión;
- registro de barreras y acomodaciones;
- protocolo de administración revisado;
- decisiones sobre riesgos aceptados y límites pendientes;
- evidencia de participación y salvaguardas.

### Puerta 3

- [ ] Las personas pueden explicar qué significa y qué no significa la salida.
- [ ] Las barreras críticas están corregidas o limitadas.
- [ ] Las condiciones de administración y desviaciones son registrables.
- [ ] La adaptación para jóvenes y menores es adecuada al contexto aprobado.
- [ ] La versión de investigación está identificada y congelada.

## Etapa 4 — Perfiles educativos y matriz de especificación

### Trabajo

1. Crear un `program_profile` por programa autorizado o marcarlo como pendiente.
2. Registrar actividades, énfasis, contexto, sitio, nivel, modalidad, disponibilidad, fuentes, revisores, disensos y límites de afirmación.
3. Separar hechos del catálogo, descripción educativa, hipótesis de orientación y evidencia psicométrica.
4. Definir constructos, intereses, preferencias y contexto que se quieren explorar.
5. Redactar contenido original y documentar proveniencia, adaptación y revisión.
6. Conectar cada ítem o tarea con una celda de la matriz de especificación, una razón y una limitación.
7. Preespecificar faltantes, acomodaciones, incertidumbre, empates y condiciones en las que no se ordenará la salida.

### Producir

- perfiles educativos versionados;
- matriz de especificación de orientación;
- banco de contenido original;
- reglas de puntuación y afinidad como hipótesis revisables;
- mapa de razones, fuentes y límites;
- plan de análisis y replicación.

### Puerta 4

- [ ] Todo perfil tiene fuente, versión, responsable, revisión y límites de afirmación.
- [ ] Todo contenido es original o tiene derechos documentados.
- [ ] La comparación cubre el catálogo autorizado, sin pre-filtro obligatorio de facultad.
- [ ] La puntuación y la afinidad no dependen de reglas arbitrarias del cliente.
- [ ] El resultado previsto es plural, explicable y con incertidumbre.

## Etapa 5 — Piloto exploratorio

### Trabajo

- describir muestra, cobertura, acceso, idioma, modalidad, faltantes y acomodaciones;
- congelar catálogo, perfiles, contenido y reglas antes del análisis;
- comprobar que la misma entrada y versiones producen el mismo resultado cuando esa propiedad sea parte del diseño;
- medir comprensión de razones, incertidumbre, límites y preguntas de siguiente paso;
- estudiar utilidad percibida sin tratar la aceptación de una carrera como criterio de éxito;
- revisar subgrupos, sitio, nivel, modalidad, idioma y disponibilidad con resultados negativos y mixtos;
- preservar una estrategia de réplica o muestra de confirmación cuando sea viable;
- registrar todo cambio como una nueva versión.

### Producir

- informe de calidad y condiciones;
- informe de comprensión, respuesta-proceso y utilidad;
- informe de afinidades, incertidumbre y faltantes;
- revisión de accesibilidad y equidad;
- registro de cambios;
- argumento preliminar de interpretación y uso.

### Puerta 5

- [ ] La salida se entiende como exploración y no como decisión.
- [ ] La muestra y sus límites están explícitos.
- [ ] La pluralidad de opciones no oculta empates o falta de evidencia.
- [ ] La aceptación o satisfacción no se usa como prueba única de validez.
- [ ] Un hallazgo negativo o mixto produce revisión, una afirmación más estrecha o una pausa.

## Etapa 6 — Validez, equidad, accesibilidad y generalización

### Plan de evidencia

| Evidencia | Pregunta |
| --- | --- |
| Catálogo y perfiles | ¿Los programas y perfiles provienen de versiones autorizadas y trazables? |
| Contenido y matriz de especificación | ¿Las preguntas representan los dominios definidos? |
| Respuesta-proceso | ¿Las personas comprenden instrucciones, razones, incertidumbre y límites? |
| Precisión y estructura | ¿Las puntuaciones son suficientemente precisas y coherentes para el uso declarado? |
| Relaciones con variables | ¿Las relaciones son pertinentes y están estimadas con diseño adecuado? |
| Uso y consecuencias | ¿La salida ayuda a explorar sin inducir una decisión indebida? |
| Equidad y accesibilidad | ¿Se revisan barreras, idioma, acomodaciones, precisión por subgrupo, `DIF` o invarianza cuando corresponda? |
| Generalización | ¿La evidencia cubre la UAGRM o solo determinados sitios, niveles, modalidades y poblaciones? |

### Trabajo

- congelar preguntas centrales antes de buscar resultados favorables;
- estudiar interpretaciones alternativas y límites de transporte;
- documentar evidencia negativa, mixta y faltante;
- replicar fuera de la primera facultad o sitio cuando la afirmación sea más amplia;
- revisar profesional, institucional, ética, privacidad, accesibilidad y legalmente según riesgo;
- definir monitoreo, revalidación y condiciones de pausa.

### Puerta 6

- [ ] El argumento respalda una interpretación y uso específicos, no solo una puntuación.
- [ ] Se informa qué parte de la UAGRM está representada y cuál no.
- [ ] Equidad, accesibilidad, comprensión y consecuencias fueron revisadas.
- [ ] No hay afirmaciones de admisión, éxito, empleabilidad, diagnóstico o alto impacto.
- [ ] Se definieron revalidación, monitoreo y pausa.

## Etapa 7 — Candidato de operación de bajo riesgo

Esta etapa no autoriza por sí sola software. Solo prepara una decisión de implementación si existe evidencia suficiente.

### Controles a demostrar

- versiones de contenido, perfiles, puntuación, afinidad y reporte;
- acceso mínimo, auditoría y protección de datos;
- consentimiento/asentimiento, acomodaciones y ruta de contacto;
- reporte con razones, incertidumbre, límites y preguntas de exploración;
- monitoreo de usos inesperados, reclamos, barreras, faltantes y cambios de catálogo;
- suspensión ante riesgo material de validez, equidad, seguridad o privacidad;
- documentación de cómo continuar si Engram no está disponible: `AGENTS.md`, OpenSpec y documentos del repositorio serán la base [S32]–[S38].

### Puerta 7

- [ ] Existe aprobación explícita para planificar una implementación de bajo riesgo.
- [ ] Los controles de datos fueron probados o existe evidencia de que siguen pendientes.
- [ ] La responsabilidad de monitoreo y pausa tiene nombre.
- [ ] El alcance de la implementación futura está escrito por repositorio.
- [ ] Se mantiene la independencia entre el catálogo institucional, la evidencia psicométrica y el contexto auxiliar.

## Etapa 8 — Implementación futura, condicionada

Solo después de las puertas anteriores se puede proponer un cambio de software. Cada repositorio tendrá su propio cambio OpenSpec y su propia revisión; ya usa memorias de investigación externas separadas en Engram, y los cambios coordinados usarán un ID cruzado y enlaces recíprocos. El backend será dueño del contrato de dominio/API y el frontend lo consumirá; ningún repositorio inventará el contrato del otro.

La documentación portátil futura será un `AGENTS.md` por repositorio, no una copia de Gentle AI. Debe cubrir propósito, seguridad, lectura, significado de OpenSpec, protocolo de Engram o degradación, comandos y pruebas solo cuando existan y estén verificados, coordinación, y reporte de finalización o bloqueo. Debe excluir instrucciones de persona, comandos slash, definiciones de subagentes, registros de revisión, recibos, identificadores `lineage`, lentes y maquinaria interna de Gentle AI [S35].

No se debe iniciar una fase porque un documento diga “listo”. La autorización requiere una decisión humana, evidencia enlazable y un alcance explícito.

## Matriz de generalización

| Evidencia | Afirmación máxima provisional |
| --- | --- |
| Conceptual | Hipótesis y matriz de especificación; no instrumento validado, norma ni corte. |
| Piloto de un sitio/facultad | Hallazgos preliminares para la población y condiciones estudiadas. |
| Replicación entre facultades o sitios | Afirmaciones acotadas a las condiciones replicadas; no transferencia automática a toda la UAGRM. |
| Cobertura UAGRM con muestra pertinente | Afirmaciones limitadas a población, idioma, modalidad y uso efectivamente estudiados. |
| Validación multiinstitucional | Afirmaciones solo para instituciones, regiones y propósito investigados; no norma nacional automática. |
| Monitoreo | Continuidad condicionada a evidencia, gobierno, revalidación y ausencia de riesgos materiales. |

## Decisiones pendientes

| Decisión | Por qué importa | Estado |
| --- | --- | --- |
| Población inicial | Determina muestreo, consentimiento, accesibilidad y generalización. | Pendiente de aprobación institucional. |
| Marco completo de catálogo | Determina programas, IDs, estado, disponibilidad y perfiles. | Pendiente de reconciliación; [S29] y [S30] no son equivalentes. |
| Cobertura por etapas | Permite organizar investigación sin convertirla en pre-filtro de recomendación. | Pendiente de plan y responsables. |
| Modalidad e idioma | Cambian acceso, respuesta-proceso y comparabilidad. | Pendiente. |
| Menores y jóvenes | Determina comprensión, consentimiento/asentimiento y salvaguardas. | Pendiente cuando la población los incluya. |
| Constructos y medidas | Determinan contenido, puntuación, evidencia y límites. | Pendiente de la matriz de especificación. |
| Forma de salida | Determina pluralidad, orden, empates, razones e incertidumbre. | Mantener conjunto u orden exploratorio; falta evidencia. |
| Privacidad y retención | Determinan si se puede recolectar y reportar información. | Requiere revisión institucional y legal. |
| Dependencias y arquitectura | Cambian riesgo, mantenimiento y capacidad de validación. | Solo hipótesis; no hay decisiones sobre la pila tecnológica. |
| Revalidación y pausa | Protegen frente a la deriva, cambios de catálogo y uso indebido. | Pendiente. |

## Criterios de detención

Pausar recolección, puntuación, comparación o planificación de implementación cuando:

- cambie el propósito, la población o el nivel de riesgo sin nueva revisión;
- se use una fuente de catálogo no autorizada o sin versión;
- una afinidad se presente como admisión, éxito, empleabilidad, diagnóstico o decisión;
- aparezca una barrera material de accesibilidad, privacidad, seguridad o equidad;
- la precisión sea insuficiente para la interpretación propuesta;
- se oculten hallazgos negativos o se transforme una hipótesis en regla;
- se solicite una decisión de alto impacto;
- una dependencia, repositorio o herramienta introduzca un riesgo no resuelto;
- una fase futura no tenga puerta aprobada, responsable y evidencia verificable.

La respuesta correcta es estrechar la afirmación, corregir el diseño, recolectar evidencia apropiada o detenerse; no cubrir la incertidumbre con una interfaz más pulida.
