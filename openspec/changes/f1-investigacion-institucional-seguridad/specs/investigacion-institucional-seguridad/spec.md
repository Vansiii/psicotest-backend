# Delta para investigacion-institucional-seguridad

## Identidad del cambio

- project_id: `psicotest-backend`
- cross_repo_change_id: `f1-investigacion-institucional-seguridad`
- related_project: `psicotest-frontend`
- responsable provisional: Marces
- Contrato: el backend será propietario futuro del contrato de dominio/API; el frontend no puede inventar ese contrato y solo lo consumirá cuando esté publicado y versionado.
- Puertas 0 y 1: NO aprobadas. Este spec documenta los requisitos de la INVESTIGACIÓN; crearlo no aprueba las puertas.
- Naturaleza: cambio de investigación (documentar, consultar, decidir y registrar). Sin código, API, infraestructura, autenticación ni base de datos.

## ADDED Requirements

### Requirement: Propósito de orientación exploratoria y de bajo riesgo

La fase DEBE documentar el propósito como orientación vocacional/educativa exploratoria y de bajo riesgo, con salida plural (afinidades, razones, incertidumbre, limitaciones, preguntas). NO DEBE afirmarlo como aprobado institucionalmente.

#### Scenario: Propósito registrado como hipótesis pendiente de aprobación

- GIVEN que no existe aprobación institucional formal del propósito
- WHEN se documenta el propósito de la fase
- THEN se registra como propósito propuesto, sujeto a aprobación de la puerta 0
- AND no se afirma aprobación institucional alguna

### Requirement: Poblaciones como grupos distintos

Las poblaciones previstas (secundaria, postulantes, otras personas interesadas) DEBEN tratarse como poblaciones distintas cuando corresponda, con comprensión, consentimiento, lenguaje y riesgos propios. Los participantes de investigación DEBEN registrarse aparte.

#### Scenario: Poblaciones no intercambiables

- GIVEN que una decisión de investigación afecta a estudiantes de secundaria
- WHEN se registra la decisión
- THEN se documenta con el tratamiento específico de esa población
- AND no se extrapola el tratamiento de postulantes ni de adultos

### Requirement: Partes interesadas pendientes de confirmación

El mapa de responsables DEBE registrarse como PENDIENTE DE CONFIRMACIÓN por área (orientación, facultades, programas, accesibilidad, ética, registros, tecnología, privacidad). NO DEBE inventar nombres, cargos ni autoridades.

#### Scenario: Responsable no confirmado

- GIVEN que un área institucional aún no confirmó a su responsable
- WHEN se actualiza el mapa de partes interesadas
- THEN se registra el área como PENDIENTE DE CONFIRMACIÓN
- AND no se asigna nombre, cargo ni autoridad

### Requirement: Consentimiento y asentimiento para menores

El procedimiento de consentimiento/asentimiento DEBE investigarse específicamente para menores cuando corresponda (edades, quién consiente, quién asiente, verificación de comprensión, acompañamiento). NO DEBE asumirse que el procedimiento de adultos es suficiente.

#### Scenario: Procedimiento de menores no derivado del de adultos

- GIVEN que el procedimiento de adultos existe como referencia
- WHEN se documenta el procedimiento para menores
- THEN se investiga y registra un procedimiento específico de consentimiento/asentimiento
- AND no se asume que el de adultos es suficiente

### Requirement: Gobierno de datos sujeto a revisión institucional y legal

DEBEN documentarse minimización, retiro, acceso, retención y eliminación de datos. NO DEBE decidirse ninguna política de datos sin base institucional o legal verificable.

#### Scenario: Política de datos sin revisión concluida

- GIVEN que la revisión institucional/legal aún no concluyó
- WHEN se documenta retención y eliminación
- THEN se registran como pendientes de revisión, sin plazos decididos

### Requirement: Accesibilidad y contexto de las poblaciones

DEBEN estudiarse accesibilidad, contexto cultural y lingüístico, dispositivos y conectividad de las poblaciones previstas, sin inventar barreras ni acomodaciones.

#### Scenario: Estudio de contexto sin datos propios

- GIVEN que no hay datos propios de dispositivos ni conectividad
- WHEN se documenta el estudio de accesibilidad y contexto
- THEN se registran como evidencia faltante, sin afirmar capacidad existente

### Requirement: Usos prohibidos registrados

La fase DEBE registrar como prohibidos: admisión o matrícula automática, elegibilidad, éxito académico, empleabilidad, diagnóstico clínico y decisiones de alto impacto. NO DEBE proponer ningún comportamiento que habilite esos usos.

#### Scenario: Lista de usos prohibidos sin comportamiento

- GIVEN que un documento futuro sugiere un uso de alto impacto
- WHEN se revisa contra los usos prohibidos
- THEN se rechaza y se registra el conflicto en el registro de riesgos

### Requirement: Cobertura de toda la oferta autorizada

DEBE registrarse que la cobertura futura alcanza TODA la oferta autorizada de la UAGRM. El escalonamiento por facultad/sitio DEBE registrarse como estrategia de cobertura y NO DEBE convertirse en pre-filtro obligatorio de recomendación.

#### Scenario: Escalonamiento como estrategia, no filtro

- GIVEN que se propone iniciar la cobertura por una facultad
- WHEN se registra la estrategia de escalonamiento
- THEN se documenta como estrategia de investigación, no como pre-filtro

### Requirement: Discrepancia de catálogo registrada sin cifra oficial

La discrepancia entre [S29] (18 facultades, 69 programas) y [S30] (~80 entradas con repeticiones) DEBE registrarse sin elegir cifra oficial. La fuente institucional autorizada DEBE quedar pendiente de identificación.

#### Scenario: Discrepancia documentada sin resolución

- GIVEN que [S29] y [S30] difieren en alcance
- WHEN se registra el catálogo en el cambio
- THEN se documenta la discrepancia sin elegir cifra
- AND se marca la fuente autorizada como evidencia faltante

### Requirement: Registro de riesgos, decisiones pendientes y evidencia faltante

DEBEN proponerse un registro de riesgos (daño, mitigación, responsable, evidencia, estado), un mapa de decisiones pendientes (qué decidir, quién decide, evidencia necesaria, bloqueo) y un registro de evidencia faltante.

#### Scenario: Evidencia faltante registrada como bloqueo

- GIVEN que una decisión crítica carece de evidencia
- WHEN se actualiza el mapa de decisiones
- THEN la decisión se registra como bloqueada por evidencia faltante

### Requirement: Propiedad futura del contrato de dominio y API

El backend DEBE declararse propietario futuro del contrato de dominio/API. El frontend NO DEBE inventar ese contrato; DEBE consumirlo solo cuando el backend lo publique y versione.

#### Scenario: El frontend no define el contrato

- GIVEN que el frontend propone campos o reglas de contrato
- WHEN se registra la interacción backend/frontend
- THEN no se incorpora la propuesta como contrato
- AND se registra que el contrato lo publica y versiona el backend

### Requirement: Cierre de la fase alineado a las puertas 0 y 1

Los criterios de cierre DEBEN alinearse a las casillas de las puertas 0 y 1 (aprobaciones verificables, responsables confirmados, protocolos, evidencia enlazable). La falta de respuesta institucional DEBE reportarse como bloqueo; NO DEBE inferirse aprobación ni avanzarse.

#### Scenario: Cierre bloqueado por falta de respuesta institucional

- GIVEN que la institución no respondió en el plazo definido
- WHEN se revisa el cierre de la fase
- THEN se reporta bloqueo y no se avanza a la siguiente fase
- AND no se infiere aprobación alguna

### Requirement: Fase sin tareas de programación

Las tareas futuras del cambio DEBEN ser de investigación, consulta, documentación y decisión. NO DEBE haber tareas de programación, diseño técnico ni infraestructura.

#### Scenario: Tarea de programación rechazada

- GIVEN que se propone una tarea de programación dentro del cambio
- WHEN se planifican las tareas de la fase
- THEN se rechaza y se la registra fuera del alcance de la fase

### Requirement: Artefactos en español neutral y profesional

Todos los artefactos de la fase DEBEN redactarse en español neutral y profesional, con palabras clave DEBE/NO DEBE/DEBERÍA/PUEDE para distinguir obligaciones de opciones.

#### Scenario: Redacción del registro en español profesional

- GIVEN que se redacta un registro de la investigación
- WHEN se revisa el artefacto
- THEN cumple el idioma y registro definidos, sin variantes coloquiales
