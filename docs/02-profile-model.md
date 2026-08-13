# Modelo de perfil educativo y orientación para toda la UAGRM

**Decisión primero:** el objeto de comparación de TestPsico es un `program_profile` educativo, revisado y versionado, para cada carrera o programa autorizado de toda la UAGRM. La facultad, el campus o sitio, el nivel, la modalidad y la disponibilidad son metadatos del catálogo y pueden servir para explicar o filtrar una exploración solicitada; ninguno es un pre-filtro obligatorio por defecto.

La salida debe ser un conjunto plural o un orden exploratorio de afinidades con razones, incertidumbre, limitaciones y preguntas para continuar la exploración. No debe afirmar “la carrera correcta”, elegibilidad o admisión, éxito académico, empleabilidad, diagnóstico clínico ni una decisión de alto impacto.

```text
contexto de orientación → constructos, intereses, preferencias y factores contextuales
→ indicadores y respuestas → medidas/puntuaciones
→ afinidades con perfiles de programa → incertidumbre y evidencia
→ retroalimentación exploratoria y preguntas de siguiente paso
```

Este documento describe un modelo de investigación. No afirma que el catálogo, los perfiles, el instrumento o las puntuaciones ya existan.

## Vocabulario de dominio

| Término | Significado y límite |
| --- | --- |
| `institution` | Institución educativa que autoriza el catálogo y el uso. En esta investigación, la UAGRM. |
| `campus` / `site` | Sede, ubicación o sitio asociado al programa. Es metadato contextual; no prueba calidad, acceso o adecuación individual. |
| `faculty` | Facultad asociada a un programa. Sirve para describir cobertura y permitir un filtro explícito, pero no restringe automáticamente la comparación. |
| `level` | Nivel o tipo de formación que el catálogo institucional defina. No equivale a una predicción de capacidad o éxito. |
| `modality` | Modalidad de estudio o administración publicada. Puede afectar la exploración y la accesibilidad, pero no es un criterio psicométrico automático. |
| `availability` | Estado y fechas de oferta, admisión o disponibilidad informadas por una fuente autorizada. No es una garantía de elegibilidad. |
| `program` | Carrera o programa académico. El dominio conserva `program`; la interfaz puede decir “carrera”. |
| `program_profile` | Perfil educativo revisado y versionado de un `program`: describe actividades, énfasis, contexto, fuentes y límites; no es un ideal de persona ni un requisito de admisión. |
| `recommendation_result` | Salida contextual de una ejecución: conjunto u orden de afinidades, razones, incertidumbre, evidencia, límites y preguntas de exploración. No es una etiqueta definitiva. |

## Ruta de trabajo

1. Confirmar propósito de orientación de bajo riesgo, poblaciones, idioma, modalidad, accesibilidad y consecuencias.
2. Reconciliar el catálogo autorizado de toda la UAGRM antes de enumerar o comparar programas.
3. Versionar cada `program_profile` con fuente, responsable, vigencia, revisión, disensos y límites de afirmación.
4. Definir constructos, intereses, preferencias y factores contextuales sin convertirlos en requisitos de selección.
5. Reportar varias afinidades o un orden exploratorio prudente, con incertidumbre, límites y preguntas para investigar opciones.

## 1. Propósito, población y contexto

El modelo debe describir qué se compara y qué puede hacer una persona con la salida, no etiquetar una esencia personal. Las poblaciones previstas incluyen:

| Población | Preguntas de investigación y salvaguardas |
| --- | --- |
| Estudiantes de secundaria | ¿Comprenden el propósito, las preguntas y los límites? ¿Qué consentimiento/asentimiento, acompañamiento y lenguaje necesitan? |
| Postulantes o personas interesadas en ingresar a la UAGRM | ¿Cómo se evita que una afinidad se interprete como admisión, elegibilidad o promesa de éxito? |
| Otras personas interesadas en realizar el test psicotécnico | ¿Qué propósito, contexto, idioma, modalidad y restricciones de uso se aplican? |
| Participantes de investigación | ¿Qué marco muestral, minimización, retiro, confidencialidad y uso posterior de datos fue aprobado? |

Registrar antes de diseñar medidas:

| Campo | Decisión requerida |
| --- | --- |
| Propósito | Orientación vocacional/educativa exploratoria y de bajo riesgo, pendiente de aprobación institucional. |
| Alcance académico | Catálogo autorizado de toda la UAGRM. Facultad, sitio, nivel, modalidad y disponibilidad son metadatos o filtros explícitos, no un filtro obligatorio. |
| Población | Poblaciones y subgrupos definidos, incluyendo edad, trayectoria educativa, idioma, acceso y necesidades de apoyo. |
| Contexto | Actividades y condiciones educativas documentadas, no un perfil laboral ni un ideal de admisión. |
| Modalidad | Presencial, en línea, abierta, supervisada u otra, con sus condiciones y acomodaciones. |
| Nivel de consecuencias | Consecuencias de interpretar mal una afinidad o de usarla fuera de orientación. |
| Uso permitido | Explorar alternativas, comprender razones, formular preguntas y orientar una conversación o siguiente paso. |
| Uso prohibido | Diagnóstico, admisión o matrícula automática, elegibilidad, contratación, rechazo, predicción determinista o decisión de alto impacto. |

La página oficial de Orientación Vocacional de la UAGRM demuestra un contexto institucional de acompañamiento, intereses, capacidades y “Test Psicotécnico”; no valida el instrumento, los ítems, las puntuaciones ni los perfiles de TestPsico [S28].

## 2. Catálogo completo y límites de evidencia

La comparación necesita un catálogo institucional autorizado, no una lista pública copiada sin reconciliación. La evidencia disponible muestra por qué el catálogo es una puerta de investigación:

- Admisiones informa 18 facultades y 69 programas de formación profesional en Santa Cruz de la Sierra [S29]. Es información institucional contextual, no necesariamente un catálogo universitario completo y no tiene metadatos confiables de versión o vigencia.
- La página pública de carreras muestra aproximadamente 80 entradas o páginas, con repeticiones por facultad o sitio y campos libres desiguales [S30]. No debe elegirse ese número como verdad del catálogo.
- La discrepancia debe resolverse con una fuente institucional autorizada, IDs estables, estado del programa, facultad, sitio, nivel, modalidad, disponibilidad, fechas de vigencia/efectividad, responsable y versión.

Antes de cualquier recomendación, el registro debe reconciliar duplicados, alias, programas repetidos por ubicación y diferencias entre páginas. Si un programa o su estado no está respaldado por una versión autorizada, queda fuera de la comparación hasta que se resuelva; esto es una regla de calidad de datos, no un pre-filtro por facultad.

### Registro mínimo de catálogo

| Campo | Registro mínimo |
| --- | --- |
| Alcance | `institution_id`, `program_id`, `faculty_id`, `campus_id` o `site_id` cuando corresponda, nivel y modalidad. |
| Identidad | ID estable, nombre oficial, alias documentados y relación con páginas o fuentes. |
| Oferta | Estado, disponibilidad, fecha de inicio y fin de vigencia/efectividad cuando la institución lo defina. |
| Fuente | URL o documento, fecha de consulta, versión, responsable y método de reconciliación. |
| Revisión | Estado de revisión, aprobador institucional, disensos y datos faltantes. |
| Límite | Qué puede describir el registro y qué no dice sobre una persona. |

## 3. `program_profile`: perfil educativo, no perfil de persona

Cada `program_profile` debe describir, con lenguaje revisable:

- actividades y contextos educativos documentados;
- contenidos, énfasis o experiencias formativas que la institución decida comunicar;
- condiciones de aprendizaje, sitio, nivel, modalidad y accesibilidad;
- fuentes, fecha, versión, responsable, revisor y desacuerdos;
- afirmaciones que el perfil no permite hacer sobre una persona;
- estado de evidencia: establecido, preliminar, mixto, faltante o no establecido.

La evidencia institucional del perfil responde qué se ofrece y cómo se describe. La evidencia psicométrica responde qué significan las respuestas. La evidencia de interpretación y uso responde si la salida se comprende y sirve para explorar. Ninguna reemplaza a las otras.

No se debe convertir la opinión de una persona revisora en un rasgo del programa. Se deben conservar alternativas, disensos y fuentes faltantes, y crear una versión nueva cuando cambie una afirmación publicada.

## 4. Constructos, intereses, preferencias y factores contextuales

Para orientación, los constructos pueden organizar dominios de respuesta, intereses y preferencias, pero no describen una esencia fija ni una obligación de selección. Los KSAO —conocimientos, habilidades, capacidades y otras características— quedan como vocabulario de referencia para investigaciones futuras; no son requisitos de admisión, reglas de recomendación ni diagnóstico.

Los factores contextuales pueden incluir trayectoria educativa, condiciones de aprendizaje, idioma, acceso tecnológico, responsabilidades familiares, contexto socioeconómico declarado y preferencias de modalidad o sitio. Deben capturarse solo cuando tengan finalidad aprobada, minimización, accesibilidad y protección; no deben convertirse en determinantes ocultos.

El estudio local de 122 postulantes de Ciencias Económicas y Empresariales, realizado en marzo de 2023, fue descriptivo, transversal y no experimental; observó dimensiones personales, familiares y socioeconómicas, con predominio de factores familiares y socioeconómicos [S31]. Es una hipótesis y una fuente de contexto local, no una ponderación universal para todas las facultades, carreras o personas, ni evidencia causal.

Un indicador más defendible:

- puede observarse o elicitarse mediante una respuesta definida;
- se vincula a una actividad, contexto, interés o preferencia documentada;
- es suficientemente específico para la matriz de especificación y el análisis;
- se revisa lingüística, cultural y accesiblemente;
- declara qué no permite inferir.

| Etiqueta débil | Forma más defendible |
| --- | --- |
| “Tiene vocación para esta carrera” | “Expresa interés por actividades documentadas en este perfil, bajo las condiciones y versión registradas.” |
| “Encaja perfectamente” | “Muestra una afinidad exploratoria en dominios concretos; la salida no predice rendimiento ni satisfacción.” |
| “No sirve para esta carrera” | “No se observaron coincidencias suficientes en los dominios disponibles; faltan contexto, evidencia o alternativas para concluir.” |

## 5. Matriz de orientación y comparación

La matriz de especificación conecta respuestas, dominios de orientación y versiones de `program_profile` sin crear una regla oculta de admisión.

| Constructo, interés o preferencia | Contexto del programa | Indicador o respuesta | Medida candidata | Evidencia necesaria | Riesgo irrelevante | Límite del reporte |
| --- | --- | --- | --- | --- | --- | --- |
| Dominio de interés definido | Actividad o énfasis documentado | Preferencia o respuesta observable | Ítem, escenario, escala o comparación | Contenido, respuesta-proceso, estructura y relaciones cuando correspondan | Idioma, interfaz, tiempo, discapacidad, acceso | Qué afinidad se puede sugerir y qué no |
| Preferencia contextual | Condición educativa explícita | Elección razonada o patrón de respuesta | Respuesta estructurada | Comprensión, pertinencia, accesibilidad y revisión | Carga de lectura, opciones ausentes, presión social | No generalizar a éxito o empleabilidad |
| Contexto declarado | Sitio, nivel, modalidad o disponibilidad del catálogo | Información que la persona decide aportar | Campo contextual minimizado | Finalidad, privacidad, calidad y límites | Sesgo de disponibilidad, falta de acceso o exposición | Mostrar como contexto, no como rasgo fijo |

Para cada medida se deben especificar respuesta-proceso, puntuación, faltantes, acomodaciones, población y relación con la versión del perfil. Una escala de autoinforme, una elección estructurada y una comparación de dominios son diseños diferentes, con distintas preguntas de validez y accesibilidad [S1][S3][S6].

## 6. Afinidades, orden exploratorio e incertidumbre

La salida debe preservar pluralidad. Un orden de afinidades puede ayudar a comenzar una conversación, pero no debe ocultar empates, cobertura desigual, perfiles incompletos o incertidumbre. Si los datos no justifican ordenar, se debe devolver un conjunto de opciones o declarar que no hay evidencia suficiente.

Una futura agregación tendría que predefinir:

1. dominios incluidos y justificación;
2. dirección y transformación de cada puntuación;
3. pesos y fundamento sustantivo, sin derivarlos automáticamente de una correlación local;
4. tratamiento de faltantes, respuestas incompletas y acomodaciones;
5. propagación de incertidumbre y reglas para empates;
6. uso de metadatos como explicación o filtro explícito, nunca como autoridad oculta;
7. evidencia que habilita cada interpretación;
8. disparadores de revisión, monitoreo y suspensión.

El servidor o la capa de dominio debe controlar las reglas versionadas. La interfaz no puede enviar pesos, fórmulas, filtros obligatorios, perfiles ni una carrera objetivo para forzar el resultado.

### Contrato mínimo de `recommendation_result`

Cada resultado futuro debe conservar:

- `institution_id`, catálogo y versión de cada `program_profile`;
- conjunto o orden de programas considerados, con su estado de disponibilidad;
- dominios, razones y fuentes de cada afinidad;
- precisión, incertidumbre, faltantes, acomodaciones y desvíos;
- población, sitio, nivel, modalidad y condiciones de administración;
- estado de evidencia para interpretación y uso;
- limitaciones, advertencias y usos prohibidos;
- preguntas de exploración para investigar alternativas;
- ruta para preguntas, revisión o conversación con orientación.

La redacción debe ser condicional: “bajo estos dominios, condiciones y versiones se observaron estas afinidades”. Nunca “esta es tu carrera” o “no eres apto”.

## 7. Validación del perfil, la puntuación y el uso

| Pregunta | Aplicación en TestPsico |
| --- | --- |
| Catálogo y contenido | ¿La fuente institucional confirma el programa, su estado y la versión del perfil? Esto no valida puntuaciones. |
| Respuesta-proceso | ¿Las personas entienden preguntas, opciones, razones, incertidumbre y límites? |
| Estructura interna | ¿Los ítems o dominios se comportan como plantea la matriz de especificación? |
| Relaciones con otras variables | ¿Las relaciones son pertinentes para orientación y están estimadas con diseño e incertidumbre apropiados? |
| Interpretación y uso | ¿La persona puede usar el resultado para explorar sin convertirlo en una decisión? |
| Equidad y accesibilidad | ¿Se revisan barreras, precisión por subgrupo, idioma, acomodaciones, `DIF` o invarianza cuando corresponda? |
| Generalización | ¿La evidencia cubre población, facultad, sitio, nivel, modalidad y disponibilidad declarados? |

La evidencia local [S31] puede orientar preguntas de muestreo y contexto. No autoriza pesos universales. La cobertura por facultad o sitio puede ser escalonada para hacer viable la investigación, pero toda recomendación autorizada debe apuntar al catálogo completo vigente y declarar qué partes de la oferta o población aún no tienen evidencia.

## 8. Retroalimentación y reporte

El reporte debe ayudar a comprender afinidades acotadas y formular un siguiente paso. Como mínimo debe incluir:

- propósito, población, fecha, modalidad y versiones;
- alcance del catálogo y metadatos utilizados para explicar o filtrar;
- varias afinidades o un orden exploratorio, sin presentar una única respuesta correcta;
- razones comprensibles, fuentes, evidencia, precisión e incertidumbre;
- información faltante, acomodaciones y preocupaciones de validez;
- preguntas de exploración, enlaces o conversación sugerida cuando estén aprobados;
- limitaciones y usos prohibidos;
- tratamiento de datos, retención, acceso y ruta de revisión.

La aceptación, preferencia o satisfacción declarada por una persona puede aportar evidencia de comprensión o utilidad, pero no prueba por sí sola que un programa sea correcto, que la puntuación sea válida o que exista éxito futuro.

## 9. Anti-patrones

| Anti-patrón | Por qué falla | Reemplazo |
| --- | --- | --- |
| Empezar con una facultad obligatoria | Convierte una decisión de cobertura en una restricción arbitraria y oculta opciones de toda la UAGRM. | Catálogo completo; filtros opcionales de metadatos y cobertura explícita. |
| Elegir entre “18”, “69” o “aproximadamente 80” como catálogo final | Las fuentes tienen alcances y duplicados distintos [S29][S30]. | Reconciliar un catálogo autorizado, versionado y con IDs estables. |
| Tratar `fit` como propiedad | Oculta dominios, contexto e incertidumbre. | Afinidades plurales, razones y límites. |
| Usar un catálogo como prueba psicométrica | La oferta no valida puntuaciones ni interpretación. | Mantener registros institucionales y psicométricos separados. |
| Usar el estudio local como peso universal | Un estudio descriptivo de una facultad no generaliza ni prueba causalidad [S31]. | Convertirlo en hipótesis y replicar con muestreo adecuado. |
| Reportar una única carrera “correcta” | Crea falsa certeza y una decisión de alto impacto. | Conjunto u orden exploratorio, alternativas y preguntas. |
| Convertir sitio, modalidad o disponibilidad en aptitud | Un metadato no es evidencia de capacidad, acceso o éxito. | Mostrarlo como contexto y verificar información oficial. |
| Tratar confiabilidad como validez | Consistencia no demuestra interpretación ni uso. | Argumento de evidencia múltiple. |
| Ocultar incertidumbre | El redondeo transforma evidencia ambigua en certeza. | Mostrar precisión, faltantes y límites. |
| Copiar ítems, claves o reglas protegidas | Introduce riesgos legales, éticos y de seguridad. | Contenido original y proveniencia. |

## 10. Esquema conceptual de `program_profile`

Este YAML es vocabulario de investigación, no un contrato de implementación ni una especificación de puntuación validada.

```yaml
program_profile:
  id: "example.program-profile"
  version: "0.1-borrador"
  status: "research-only"
  purpose: "Describir un programa académico para orientación exploratoria de bajo riesgo"
  intended_use: "Exploración vocacional/educativa y conversación de siguiente paso"
  scope:
    institution_id: "uagrm-pendiente"
    catalog_version: "catalog-pendiente"
    program_id: "program-pendiente"
    faculty_id: "faculty-pendiente"
    campus_or_site_id: null
    level: null
    modality: null
    availability:
      status: "pendiente-de-fuente-autorizada"
      effective_from: null
      effective_to: null
  comparison_policy:
    catalog_scope: "Toda la oferta UAGRM autorizada y versionada"
    faculty_site_level_modality: "Metadatos o filtros explícitos; no pre-filtro obligatorio"
  context:
    language: "Español; adaptación, comprensión y acceso por revisar"
    educational_activities: []
    documented_emphases: []
    generalization_boundary: "La evidencia de un piloto no generaliza automáticamente a toda la UAGRM"
  prohibited_use:
    - "Diagnóstico clínico"
    - "Admisión, elegibilidad o matrícula automática"
    - "Contratación, rechazo laboral o decisión de alto impacto"
    - "Afirmar una carrera correcta o un resultado determinista"
  evidence_sources:
    catalog_source: "Por registrar; requiere fuente institucional autorizada"
    profile_review: "pendiente"
    psychometric_evidence: "pendiente; separada de la evidencia del catálogo"
    local_context_hypotheses:
      - "S31: contexto local, no ponderación universal"
  constructs:
    - id: "orientation-domain-1"
      type: "interes-o-preferencia"
      definition: null
      boundaries: []
      ksao_reference: null
      indicators: []
  measures:
    - id: "measure-1"
      construct_ids: []
      format: null
      provenance: "Contenido original requerido"
      scoring_rule: null
      response_process_evidence: null
      accessibility_risks: []
      status: "aun-no-pilotado"
  scoring:
    domain_scores: []
    composite: null
    missing_data_rule: null
    uncertainty_method: null
    classification_rules: "Ninguna establecida"
  recommendation:
    method: "Comparación plural, explicable y provisional con reglas versionadas"
    output: "Conjunto u orden exploratorio de afinidades; no una respuesta única"
    allowed_scope: "Programas presentes en el catálogo UAGRM autorizado"
    optional_metadata_filters: []
    reasons: []
    exploration_prompts: []
    uncertainty_and_limits: "Requerido"
  validation:
    catalog_reconciliation: "pendiente"
    content: "pendiente"
    response_process: "pendiente"
    internal_structure: "pendiente"
    interpretation_and_use: "pendiente"
    fairness_and_accessibility: "pendiente"
    generalization_to_uagrm: "pendiente"
    consequences_and_monitoring: "pendiente"
  reporting:
    audience: []
    score_explanation: "Requerido"
    affinity_explanation: "Requerido"
    uncertainty_and_limits: "Requerido"
    exploration_prompts: "Requerido"
    feedback_route: null
  governance:
    qualified_users: null
    consent_or_assent: null
    privacy_and_retention: null
    versioning_and_audit: null
```

## 11. Ejemplo ilustrativo de salida plural

El siguiente ejemplo es ficticio y no contiene nombres de carreras ni resultados de UAGRM. Solo muestra cómo comunicar varias afinidades sin afirmar una decisión.

```yaml
recommendation_result:
  id: "illustrative.recommendation-result"
  status: "illustrative-only"
  catalog_version: "catalog-example-v1"
  scope:
    institution_id: "institution-example"
    faculty_id: null
    campus_or_site_id: null
    level: null
    modality: "modalidad-de-ejemplo"
  considered_programs:
    - program_id: "program-example-a"
      affinity: "preliminary"
      relative_position: 1
      reasons:
        - "Coincidencia exploratoria con un interés declarado y una actividad ficticia documentada"
      uncertainty: "La precisión y la cobertura del perfil requieren investigación"
    - program_id: "program-example-b"
      affinity: "preliminary"
      relative_position: 2
      reasons:
        - "Coincidencia parcial en otro dominio; se recomienda comparar la actividad real"
      uncertainty: "No se debe interpretar como diferencia concluyente"
  limitations:
    - "No determina la carrera correcta, admisión, éxito, empleabilidad ni elegibilidad"
    - "El ejemplo no representa un catálogo ni una norma institucional"
  exploration_prompts:
    - "¿Qué actividades de cada programa te gustaría observar o conversar con orientación?"
    - "¿Qué información del sitio, nivel o modalidad necesitas verificar en la fuente oficial?"
```

La salida de producción requeriría catálogo reconciliado, perfiles revisados, contenido original, respuesta-proceso, accesibilidad, precisión, evidencia psicométrica, validación de interpretación y uso, y salvaguardas institucionales. Ninguno de esos elementos se presume existente.
