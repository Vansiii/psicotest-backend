# Documentación de investigación de TestPsico

**Estado:** investigación únicamente; ninguna fase de implementación ha comenzado.

TestPsico estudia una orientación vocacional/educativa de bajo riesgo para carreras y programas de toda la UAGRM. Las poblaciones previstas incluyen estudiantes de secundaria, postulantes y otras personas interesadas, sujetas a muestreo, accesibilidad, consentimiento/asentimiento y aprobación institucional.

La salida futura debe mostrar un conjunto plural o un orden exploratorio de afinidades, razones, incertidumbre, limitaciones y preguntas de siguiente paso. Nunca debe afirmar “la carrera correcta”, admisión, elegibilidad, éxito académico, empleabilidad, diagnóstico clínico ni una decisión de alto impacto.

Facultad, campus o sitio, nivel, modalidad y disponibilidad son metadatos del catálogo. Pueden explicar o filtrar una búsqueda explícita, pero no son un pre-filtro obligatorio de recomendación.

## Estado técnico futuro

Existen dos repositorios Git independientes y vacíos: `psicotest-frontend` y `psicotest-backend`.

- Cada repositorio tendrá su propio `openspec/` cuando la implementación sea autorizada; no se ha inicializado ninguno.
- Ya se usan contextos y memorias de investigación curados en Engram, separados para `psicotest-frontend` y `psicotest-backend`, incluida la decisión de alcance de toda la UAGRM. No se ha creado `.engram/config.json` ni otro archivo local en los repositorios; la identidad determinista por repositorio mediante ese archivo y un `project_name` explícito queda pendiente. Engram aporta continuidad contextual, no es fuente normativa ni almacén de datos de participantes.
- Cada repositorio tendrá una guía raíz portátil `AGENTS.md`; no se crea en esta etapa.
- Los cambios cruzados usarán un ID común, artefactos OpenSpec separados, enlaces recíprocos y memorias separadas.
- El backend será dueño futuro del contrato de dominio/API; el frontend lo consumirá.
- Si Engram no está disponible, se continuará desde `AGENTS.md`, OpenSpec, Git y la documentación del repositorio, informando la degradación.
- Las guías portátiles no dependerán de personas, instrucciones, comandos slash, subagentes, recibos de revisión, identificadores `lineage`, lentes ni mecanismos internos de Gentle AI.

## Orden de lectura

1. [01 — Fundamentos psicométricos](./01-psychometric-foundations.md): constructos, validez, precisión, equidad, accesibilidad y generalización.
2. [02 — Modelo de perfil](./02-profile-model.md): catálogo completo, `program_profile`, dominios, afinidades y reportes cautelosos.
3. [03 — Referencias y repositorios](./03-references-and-repositories.md): fuentes normativas, evidencia UAGRM, OpenSpec, `AGENTS.md`, Engram e inspiración técnica.
4. [04 — Plan de investigación](./04-research-plan.md): muestreo, reconciliación del catálogo, respuesta-proceso, pilotos y puertas previas a implementación.
5. [05 — Arquitectura candidata](./05-stack-tecnologico-y-arquitectura.md): límites de los dos repositorios, contratos y decisiones técnicas aún abiertas.
6. [06 — Reparto futuro por fases](./06-reparto-de-implementacion-por-fases.md): responsables provisionales, entregas y las seis fases marcadas como **NO INICIADAS**.

## Evidencia institucional y límites

- La página oficial de Orientación Vocacional de UAGRM demuestra contexto institucional y menciona un “Test Psicotécnico”; no valida el instrumento de TestPsico [S28].
- Admisiones informa 18 facultades y 69 programas en su alcance publicado [S29].
- La página de carreras expone aproximadamente 80 entradas o páginas, con repeticiones y campos desiguales [S30].
- La discrepancia exige un catálogo institucional autorizado, versionado, reconciliado y con IDs estables antes de recomendar.
- El estudio local de 122 postulantes de Ciencias Económicas y Empresariales es contexto e hipótesis, no evidencia generalizable ni causal para toda la UAGRM [S31].

## Alcance y no objetivos

Esta documentación cubre fundamentos psicométricos, perfiles educativos, catálogo y fuentes, investigación, arquitectura candidata y coordinación futura. No crea aplicación, API, infraestructura, datos de prueba, baremos, roles, comandos, pruebas ni normas.

No diagnostica, no selecciona, no decide admisión o elegibilidad, no predice éxito o empleabilidad, no define cortes y no reemplaza revisión profesional, institucional, ética, legal, de privacidad o accesibilidad.
