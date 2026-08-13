# Exploración: Fase 1 — Investigación institucional y límites de seguridad

## Identidad del cambio

- project_id: `psicotest-backend`
- cross_repo_change_id: `f1-investigacion-institucional-seguridad`
- related_project: `psicotest-frontend`
- responsable provisional: Marces
- Contrato: el backend será propietario futuro del contrato de dominio/API; el frontend no puede inventar ese contrato, solo consumirlo cuando esté publicado y versionado.
- Estado de la fase de producto: **NO INICIADA** — las puertas 0 y 1 del plan de investigación NO están aprobadas. Los artefactos SDD documentan la investigación; crearlos no aprueba las puertas.

## Contexto de la Fase 1

TestPsico es una iniciativa de investigación para orientación vocacional/educativa exploratoria y de bajo riesgo sobre carreras y programas autorizados de toda la UAGRM. Ambos repositorios están vacíos y sin fases de implementación iniciadas.

La Fase 1 del producto es "Investigación institucional y límites de seguridad": dejar aprobados el propósito de bajo riesgo, las poblaciones, las partes interesadas, el gobierno de datos, el catálogo pendiente de reconciliación y los usos prohibidos **antes de diseñar software** (docs/06). Su condición mínima de inicio es tener aprobadas las puertas 0 y 1 de `docs/04-research-plan.md`, lo cual NO ha ocurrido.

Las fases SDD (explore, proposal, spec, design, tasks) son el flujo interno que documenta la investigación; no son fases del producto y no las aprueban.

## Hallazgos de los documentos

### Qué está decidido (respaldado por los docs como decisión vigente)

- **Propósito (hipótesis aprobada para investigación):** orientación vocacional/educativa exploratoria y de bajo riesgo; salida plural (conjunto u orden exploratorio de afinidades, razones, incertidumbre, limitaciones y preguntas). Nunca "la carrera correcta" (docs/README, docs/01, docs/02, docs/04).
- **Poblaciones previstas:** estudiantes de secundaria, postulantes a la UAGRM y otras personas interesadas, más participantes de investigación; deben tratarse como poblaciones DISTINTAS cuando corresponda (docs/02 §1, docs/04 Etapa 1).
- **Cobertura:** toda la oferta autorizada de la UAGRM. Facultad, campus/sitio, nivel, modalidad y disponibilidad son metadatos o filtros explícitos; la cobertura gradual por facultad/sitio es estrategia de investigación, NO pre-filtro obligatorio de recomendación (docs/01 §6, docs/02 §1, docs/04 Etapa 1).
- **Usos prohibidos (listado vigente):** diagnóstico clínico, admisión o matrícula automática, elegibilidad, éxito académico, empleabilidad, contratación/rechazo, predicción determinista y cualquier decisión de alto impacto (docs/02 §1, docs/04 Etapa 0).
- **Discrepancia de catálogo registrada:** [S29] Admisiones (18 facultades, 69 programas) vs [S30] página de carreras (~80 entradas con repeticiones). Decisión: NO elegir una cifra oficial; se requiere fuente institucional autorizada, reconciliada y versionada (docs/01 §6, docs/02 §2, docs/04 Etapa 2).
- **Separación de líneas de evidencia:** catálogo institucional, evidencia psicométrica y evidencia de interpretación/uso permanecen separadas y versionadas (docs/01, docs/04).
- **Coordinación:** repositorios independientes; ID de cambio cruzado; OpenSpec por repositorio; el backend publica y versiona el contrato de dominio/API; el frontend lo consume sin redefinirlo (docs/05 §3, docs/06).
- **Gobierno de datos (principios):** minimización, separación identidad/respuestas, sin respuestas reales ni PII en código, datos de prueba, registros, OpenSpec ni Engram; Engram no es almacén normativo ni de participantes (docs/05 §8, docs/03 [S36]–[S38]).
- **Puertas 0 y 1 NO aprobadas:** ninguna de sus casillas está marcada en docs/04. No hay ranking, corte ni etiqueta definitiva como requisito oculto (docs/04 Puerta 0).

### Qué está propuesto (hipótesis, no decisiones)

- Pila tecnológica candidata (backend Python con marco HTTP + validación de esquemas; PostgreSQL; almacenamiento de objetos; identidad institucional; R/Python para análisis) — sin selección (docs/05 §5).
- Arquitectura candidata por responsabilidades: catálogo, `program_profile`, evaluación, puntuación, motor de afinidades, reporte, analítica (docs/05 §4).
- Modelo conceptual de datos y contrato API conceptual: vocabulario de investigación, no entidades ni endpoints existentes (docs/05 §6–§7).
- Responsables provisionales de fases futuras (Marces, Trevor, Jhamil, Juan Carlos, Piere, Ivan): coordinación, NO asignación laboral ni autoridad de aprobación (docs/06).
- `AGENTS.md` y `openspec/` futuros por repositorio; `.engram/config.json` pendiente (docs/03, docs/05).

### Qué está pendiente (bloquea la Fase 1)

- Aprobación institucional del propósito, población, nivel de consecuencias y salvaguardas.
- Partes interesadas y responsables institucionales reales (sin nombres ni autoridades asignadas).
- Consentimiento/asentimiento, retiro, minimización, acceso, retención, eliminación y ruta de preguntas (requieren revisión institucional y legal; [S24] es insumo, no asesoría legal).
- Marco muestral, plan de cobertura, protocolo de reclutamiento y salvaguardas.
- Plan de adaptación lingüística/cultural, accesibilidad, acomodaciones y respuesta-proceso.
- Catálogo autorizado reconciliado (puerta 2, fase posterior) — solo se registra la discrepancia [S29]/[S30].
- Constructos, matriz de especificación, contenido, puntuación y evidencia psicométrica (fases posteriores).

## Temas del alcance: estado, preguntas abiertas y qué consultar

### 1. Propósito de orientación exploratoria y de bajo riesgo

- **Estado según docs:** hipótesis escrita y respaldada como "propósito propuesto"; requiere aprobación institucional. [S28] demuestra contexto institucional (página de Orientación Vocacional), no validez del instrumento.
- **Preguntas abiertas:** ¿quién aprueba formalmente el propósito y el nivel de consecuencias? ¿Qué lenguaje institucional se usará? ¿Cómo se documenta la aprobación (acta, resolución, designación)? ¿Qué consecuencias concretas se prevén si una afinidad se malinterpreta?
- **Qué consultar y con quién:** unidad de Orientación Vocacional y autoridad institucional competente de la UAGRM (interlocutor sugerido por [S22]/[S28], aún por confirmar); no se inventan nombres ni cargos.

### 2. Poblaciones: secundaria, postulantes y otras personas interesadas

- **Estado según docs:** tres poblaciones previstas + participantes de investigación; docs/02 §1 exige no tratarlas como intercambiables (comprensión, consentimiento, lenguaje, riesgos distintos).
- **Preguntas abiertas:** ¿qué subgrupos y rangos etarios se incluyen primero? ¿Qué condiciones de inclusión/exclusión define la institución? ¿Cómo se diferencian "postulante" de "persona interesada"? ¿Qué muestra necesita cada población para el propósito declarado?
- **Qué consultar:** autoridades de admisión y registros, unidades de orientación, representación estudiantil y de secundaria (vía institucional), según lo que la UAGRM disponga.

### 3. Partes interesadas y responsables institucionales (POR CONFIRMAR)

- **Estado según docs:** docs/04 Etapa 0 lista áreas de responsabilidad candidatas: Orientación Vocacional, facultades, programas, accesibilidad, ética/investigación, registros, tecnología y privacidad. No hay nombres, cargos ni autoridades confirmados.
- **Preguntas abiertas:** ¿qué unidad tiene autoridad de decisión sobre cada tema? ¿Existe comité de ética/investigación aplicable? ¿Qué unidad de privacidad/protección de datos existe? ¿Cómo se escala un bloqueo?
- **Qué consultar:** cada área institucional candidata mencionada en docs/04; el estatuto vigente [S23] (RR 061/2024) como contexto de gobernanza. Todo responsable debe ser confirmado por la institución.

### 4. Consentimiento y asentimiento para menores cuando corresponda

- **Estado según docs:** exigencia escrita: protocolo específico para menores/jóvenes con revisión de comprensión, consentimiento/asentimiento y acompañamiento; NO asumir que el procedimiento de adultos es suficiente ([S24], [S25] como contexto legal; docs/01 §9, docs/04 Etapas 0–1).
- **Preguntas abiertas:** ¿qué edades integran "secundaria" y quién otorga consentimiento vs asentimiento? ¿Qué información se presenta a cada población y cómo se verifica comprensión? ¿Quién acompaña y deriva a orientación? ¿Qué datos mínimos se pueden pedir a menores?
- **Qué consultar:** marco legal boliviano aplicable (Ley 070 y normativa de protección de datos vigente), unidad de Orientación Vocacional y la ruta de revisión institucional/ética. No se redacta aún un protocolo definitivo; se investiga qué procedimiento corresponde.

### 5. Retiro, minimización, acceso, retención y eliminación de datos

- **Estado según docs:** principios escritos (minimización, separación, finalidad, transparencia); [S24] describe derechos tipo ARCO como insumo; las políticas concretas están pendientes de revisión institucional y legal. Sin datos recolectados.
- **Preguntas abiertas:** ¿qué datos son mínimos para orientación exploratoria? ¿Qué plazos de retención definen la institución y la ley? ¿Cómo se ejerce retiro/eliminación y acceso? ¿Qué ruta de solicitudes y quién la atiende? ¿Dónde viven los datos (responsable del registro)?
- **Qué consultar:** unidad de privacidad/registros de la UAGRM y asesoría legal competente ([S24] no es asesoría legal). Es decisión institucional, no del backend.

### 6. Accesibilidad, contexto cultural, dispositivos y conectividad

- **Estado según docs:** requisito de medición: no evaluar barreras irrelevantes de idioma, discapacidad, interfaz, tecnología, cultura o administración (docs/01 §7). [S26] documenta trabajo previo de accesibilidad en UAGRM (contexto). La modalidad, idioma y dispositivos reales están pendientes.
- **Preguntas abiertas:** ¿qué dispositivos, conectividad y modalidades usan realmente las poblaciones previstas? ¿Qué acomodaciones se requieren (lectores de pantalla, contraste, tiempo, lenguaje claro)? ¿Qué barreras se conocen de [S26] y cuáles faltan estudiar?
- **Qué consultar:** áreas de accesibilidad/inclusión de la UAGRM (contexto [S26]), unidades educativas de secundaria y los resultados del plan de respuesta-proceso de la Etapa 3 (fase posterior).

### 7. Usos prohibidos

- **Estado según docs:** lista escrita y consistente en todos los docs: admisión automática, elegibilidad, éxito académico, empleabilidad, diagnóstico clínico y decisiones de alto impacto; también "la carrera correcta" y predicción determinista.
- **Preguntas abiertas:** ¿quién aprueba la lista como política institucional? ¿Qué mecanismos de monitoreo detectarán usos indebidos (p. ej., una escuela usando la salida como filtro)? ¿Qué lenguaje visible se requerirá en la salida futura?
- **Qué consultar:** la misma autoridad que aprueba el propósito; la redacción definitiva del lenguaje visible se documenta, no se implementa.

### 8. Cobertura futura de TODA la oferta autorizada de la UAGRM

- **Estado según docs:** decidido: el catálogo de comparación debe cubrir toda la oferta autorizada; el escalonamiento por facultad/sitio es estrategia de cobertura y muestreo, nunca pre-filtro obligatorio (docs/01 §6, docs/04 Etapa 1, docs/06).
- **Preguntas abiertas:** ¿qué orden de despliegue sugiere la institución? ¿Cómo se declara en cada etapa qué partes de la oferta/población quedan fuera? ¿Quién autoriza el escalonamiento?
- **Qué consultar:** autoridades académicas de la UAGRM (facultades y dirección académica), sin prejuzgar el catálogo final (eso es la Fase 2 del producto).

### 9. Discrepancia [S29] vs [S30]

- **Estado según docs:** discrepancia registrada y decidido NO elegir cifra oficial: [S29] 18 facultades/69 programas (alcance publicado de admisiones) vs [S30] ~80 entradas con repeticiones (página de carreras). Ambas consultadas el 2026-08-12.
- **Preguntas abiertas:** ¿qué fuente institucional es la autorizada y quién la mantiene? ¿Por qué difieren los alcances? ¿Qué duplicados/alias/estados hay que reconciliar? (Esto es trabajo de la Fase 2 del producto, puerta 2; aquí solo se documenta la discrepancia y su necesidad de resolución.)
- **Qué consultar:** dirección de sistemas/informática y la unidad responsable de publicar la oferta; se registrará la discrepancia en la propuesta, sin resolverla.

### 10. Registro de riesgos, decisiones pendientes y evidencia faltante

- **Estado según docs:** docs/04 tiene "Decisiones pendientes" y "Criterios de detención"; docs/06 tiene "Decisiones que bloquean el tablero". No existe aún un registro formal de riesgos con mitigaciones (es un producto de la Etapa 0, Puerta 0).
- **Preguntas abiertas:** ¿qué riesgos de daño/malinterpretación se priorizan? ¿qué mitigaciones se aceptan y quién las decide? ¿qué evidencia falta para cerrar cada decisión pendiente?
- **Qué consultar:** a los responsables confirmados de cada área; el registro se elaborará en la propuesta como documento de investigación.

### 11. Responsabilidades futuras del backend

- **Estado según docs:** el backend será dueño futuro de: dominio y contratos (catálogo, perfiles, evaluación, puntuación, afinidades), API, autorización, persistencia y auditoría, versionado de reglas y resultados, exportaciones de investigación aprobadas (docs/05 §1). El frontend no envía pesos, fórmulas, perfiles ni reglas arbitrarias.
- **Preguntas abiertas (para registrar, NO resolver):** ¿qué campos del contrato de catálogo exigirá la fuente autorizada? ¿qué datos no debe contener el backend por minimización? ¿qué versión de contrato publicará? — todas condicionadas a puertas futuras.
- **Qué consultar:** nada externo aún; es responsabilidad declarada del backend, se documenta en la propuesta como alcance futuro, no como diseño.

## Decisiones confirmables hoy (respaldadas por los docs)

1. El propósito propuesto es orientación exploratoria de bajo riesgo con salida plural; no es una decisión implementada ni aprobada institucionalmente.
2. Las poblaciones previstas son secundaria, postulantes y otras personas interesadas, tratadas como distintas; participantes de investigación aparte.
3. La cobertura es toda la oferta autorizada UAGRM; el escalonamiento es estrategia, no pre-filtro.
4. Los usos prohibidos están listados (admisión automática, elegibilidad, éxito, empleabilidad, diagnóstico, alto impacto, "carrera correcta").
5. La discrepancia [S29]/[S30] se registra sin elegir cifra oficial.
6. El backend será propietario futuro del contrato de dominio/API; el frontend lo consumirá.
7. Ninguna fase de producto está iniciada; las puertas 0 y 1 no están aprobadas.
8. No existen datos, catálogo, perfiles, puntuaciones, roles, infraestructura ni contrato API.

## Supuestos (a validar, no confirmados)

- Que la UAGRM cuenta con unidades (Orientación Vocacional, ética/investigación, privacidad, accesibilidad, registros) capaces de ejercer los roles que docs/04 describe. No hay evidencia de su existencia formal ni de su disposición.
- Que [S24] (manual AGETIC) refleja el marco aplicable en Bolivia; requiere verificación legal vigente.
- Que [S26] implica capacidad de accesibilidad en UAGRM; es contexto, no compromiso.
- Que los interlocutores institucionales responderán y existen plazos razonables de aprobación; no hay plan de contingencia definido si no hay respuesta.

## Evidencia faltante y bloqueos institucionales

**Evidencia faltante:**
- Acta/resolución/designación de aprobación del propósito, población y nivel de consecuencias (Puerta 0).
- Mapa confirmado de responsables con autoridad real (Puerta 1).
- Marco legal vigente de protección de datos aplicable a la UAGRM y plazos de retención.
- Política institucional de consentimiento/asentimiento y salvaguardas para menores.
- Datos sobre dispositivos, conectividad, idioma y barreras de las poblaciones previstas.
- Fuente institucional autorizada del catálogo (bloquea la Fase 2, se registra aquí).
- Comité/ruta de revisión ética aplicable a investigación con personas.

**Bloqueos institucionales:**
- Sin aprobación institucional del propósito/población, la Fase 1 no puede completarse (puertas 0–1).
- Sin responsables confirmados, no hay escalamiento ni revisión.
- Sin ruta de privacidad/legal, no se puede definir retención/eliminación.
- Sin fuente autorizada, el catálogo permanece en discrepancia registrada.

## Riesgos

1. **Falsa sensación de avance:** completar artefactos SDD podría leerse como aprobación; las puertas 0–1 exigen decisión humana e institucional explícita.
2. **Inventar interlocutores o autoridades:** riesgo de documentar nombres/cargos no confirmados; todo responsable debe ser verificado con la UAGRM.
3. **Elegir cifra de catálogo por conveniencia:** [S29]/[S30] no son equivalentes; elegir una perpetuaría duplicados sin autoridad.
4. **Tratar el escalonamiento como filtro:** convertir la cobertura gradual en pre-filtro obligatorio contradice el propósito aprobado en los docs.
5. **Subestimar el procedimiento de menores:** aplicar el protocolo de adultos a menores invalidaría consentimiento/asentimiento y expondría a la institución.
6. **Decidir privacidad sin base legal:** definir retención/eliminación sin revisión institucional/legal crea obligaciones sin respaldo.
7. **Anticipar diseño técnico:** fijar contrato API, stack o entidades antes de las puertas convertiría hipótesis en autoridad.
8. **S31 como generalización:** usar el estudio local (122 postulantes de una facultad) como evidencia general sería un error de generalización.

## Límites: qué NO hace esta fase

- NO implementa código, API, infraestructura, autenticación, base de datos, catálogo ni instrumento.
- NO aprueba las puertas 0 y 1; solo documenta la investigación necesaria.
- NO elige cifras oficiales del catálogo ni resuelve la discrepancia [S29]/[S30].
- NO inventa nombres, cargos, autoridades, políticas, plazos ni evidencia.
- NO define la pila tecnológica, contrato API ni modelo de datos (todo sigue como hipótesis candidata).
- NO recolecta datos de participantes.
- NO modifica `psicotest-frontend` ni fuera de este repositorio.
- NO crea `proposal.md`, `specs/`, `design.md` ni `tasks.md`; esos quedan para las fases SDD siguientes.
- NO hace commits ni push.

## Recomendación de contenido para la próxima fase (proposal)

La propuesta (`proposal.md`, fase `sdd-propose`) debería:

1. Declarar el propósito de la Fase 1 como investigación institucional y de límites de seguridad, con estado NO INICIADA y puertas 0–1 pendientes.
2. Incluir el plan de descubrimiento institucional: lista de áreas a contactar (de docs/04 Etapa 0), agenda de preguntas por área y formato de registro de respuestas, sin nombres inventados.
3. Proponer la estructura del registro de riesgos y el mapa de decisiones pendientes (qué decidir, quién decide, qué evidencia se necesita).
4. Proponer la estructura del mapa de datos: minimización, retención, acceso, eliminación y ruta de solicitudes, sujeto a revisión institucional/legal.
5. Documentar la discrepancia [S29]/[S30] y el requisito de fuente autorizada para la Fase 2.
6. Fijar criterios de cierre medibles de la Fase 1: evidencias verificables de las casillas de las puertas 0 y 1 (aprobaciones, responsables, protocolos), no solo artefactos redactados.
7. Establecer el límite explícito: la propuesta no autoriza implementación; el backend solo registra responsabilidades futuras de contrato.
8. Definir qué evidencia faltante se reportará como bloqueo si la institución no responde (criterios de detención de docs/04).

**No está listo para `sdd-propose` hasta que el usuario confirme el plan de descubrimiento institucional** (áreas a contactar y formato de registro); sin esa confirmación, la propuesta inventaría el proceso de aprobación.
