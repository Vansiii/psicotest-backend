# Mapa documental de datos — Fase 1

## Estado y alcance

- **Cambio:** `f1-investigacion-institucional-seguridad`.
- **Proyecto:** `psicotest-backend`.
- **Fecha de registro:** 2026-08-13.
- **Estado:** **PENDIENTE DE REVISIÓN INSTITUCIONAL/LEGAL**.
- **Alcance:** mapa conceptual de investigación; no es esquema de base de datos, API, política vigente, contrato, procedimiento operativo ni autorización de recolección.
- **Regla de seguridad:** este repositorio no incorpora respuestas reales, datos identificables, credenciales, secretos ni contenido psicométrico no aprobado. No se fija una lista de campos productivos, roles, plazos ni canales por inferencia.
- **Puertas:** puertas 0 y 1 permanecen **NO APROBADAS**.
- **Registros relacionados:** [riesgos.md](riesgos.md), [decisiones.md](decisiones.md), [evidencia-faltante.md](evidencia-faltante.md) y [descubrimiento.md](descubrimiento.md).

La documentación disponible exige estudiar finalidad, minimización, acceso, retiro, retención, eliminación y solicitudes antes de recolectar datos identificables o sensibles. El mapa siguiente conserva esas preguntas separadas y marca lo que requiere revisión institucional/legal.

## Mapa conceptual

| Elemento | Finalidad documentada | Minimización y campos excluidos | Separación, acceso y ruta | Estado y fuente enlazable |
|---|---|---|---|---|
| Propósito y población | Investigar una orientación vocacional/educativa exploratoria y de bajo riesgo para poblaciones aprobadas; no establecer una decisión sobre una persona. | Solo podría considerarse información necesaria para la finalidad aprobada; no se define un conjunto de campos antes de la revisión. | La finalidad, población y condiciones de uso deben acompañar cualquier futuro tratamiento. | **PENDIENTE DE CONFIRMACIÓN.** [docs/04 — Etapa 0](../../../../docs/04-research-plan.md) y [spec.md — Propósito](../specs/investigacion-institucional-seguridad/spec.md). |
| Identidad y datos de contacto | Si una autoridad futura demuestra necesidad, permitir gestionar consentimiento/asentimiento, retiro, preguntas o solicitudes; la necesidad todavía no está aprobada. | No se deben incorporar datos identificables innecesarios, credenciales ni secretos. No se fijan campos concretos ni un canal. | La identidad debe mantenerse restringida y separada de respuestas, puntuaciones y resultados; el acceso autorizado sigue pendiente. | **PENDIENTE DE REVISIÓN INSTITUCIONAL/LEGAL.** [docs/01 — Privacidad](../../../../docs/01-psychometric-foundations.md) y [docs/05 — Separación y autorización](../../../../docs/05-stack-tecnologico-y-arquitectura.md). |
| Respuestas y condiciones de administración | Estudiar respuesta-proceso, comprensión, medición e incertidumbre solo para el uso investigado y aprobado. | Minimizar lo necesario; no guardar respuestas reales ni PII en este paquete documental. No se incorporan ítems o contenido no aprobado. | Deben separarse de la identidad; las condiciones de modalidad, idioma, dispositivo, acceso y acomodación requieren definición y evidencia. | **PENDIENTE DE REVISIÓN INSTITUCIONAL/LEGAL.** [docs/01 — Administración y puntuación](../../../../docs/01-psychometric-foundations.md) y [docs/04 — Etapa 3](../../../../docs/04-research-plan.md). |
| Puntuaciones y precisión | Si se autorizan en una fase futura, representar dominios y su incertidumbre bajo una versión y población explícitas. | No se deben crear puntuaciones, baremos, cortes, etiquetas definitivas ni predicciones en esta fase. | Deben conservarse separadas de la identidad y no convertirse en admisión, elegibilidad, diagnóstico, éxito, empleabilidad o decisión de alto impacto. | **PENDIENTE DE INVESTIGACIÓN Y AUTORIZACIÓN.** [docs/01 — Confiabilidad e incertidumbre](../../../../docs/01-psychometric-foundations.md) y [docs/02 — Afinidades](../../../../docs/02-profile-model.md). |
| Afinidades y reporte | Ofrecer, solo si se autoriza, un conjunto u orden exploratorio con razones, incertidumbre, limitaciones y preguntas. | Excluir afirmaciones de carrera correcta, aptitud fija, admisión, elegibilidad, éxito, empleabilidad, diagnóstico y alto impacto. | El reporte no debe añadir afirmaciones nuevas; debe conservar fuentes, versiones, límites y ruta de preguntas que la institución apruebe. | **PENDIENTE DE CONFIRMACIÓN.** [docs/02 — Retroalimentación y reporte](../../../../docs/02-profile-model.md) y [spec.md — Propiedad y cierre](../specs/investigacion-institucional-seguridad/spec.md). |
| Catálogo y perfiles educativos | Describir la oferta autorizada y los perfiles de programas como evidencia institucional separada de la medición. | No usar listas sin reconciliar, cifras elegidas por conveniencia, duplicados sin resolver ni perfiles sin fuente autorizada. | Mantener fuente, versión, estado, vigencia e identificadores; no mezclar estos registros con identidad o respuestas de participantes. | **BLOQUEADO por fuente autorizada faltante.** [docs/03 — S29 y S30](../../../../docs/03-references-and-repositories.md) y [docs/04 — Etapa 2](../../../../docs/04-research-plan.md). |
| Evidencia y auditoría futura | Conservar proveniencia, versión, población, condiciones, decisiones y límites suficientes para revisar el uso aprobado. | No guardar datos identificables, respuestas brutas, credenciales ni contenido psicométrico no aprobado en registros de investigación. | El acceso, la auditoría y las exportaciones deben limitarse a la necesidad y autorización que se definan; no existen roles actuales. | **PENDIENTE DE REVISIÓN INSTITUCIONAL/LEGAL.** [docs/05 — Seguridad, privacidad y gobernanza](../../../../docs/05-stack-tecnologico-y-arquitectura.md). |

## Reglas específicas pendientes de decisión

### Finalidad y minimización

- La finalidad propuesta **DEBE** limitarse a orientación exploratoria y de bajo riesgo, si la institución la aprueba.
- Solo se **DEBERÍA** considerar información necesaria para esa finalidad y para las salvaguardas aprobadas.
- **NO DEBE** recolectarse información para admisión, elegibilidad, diagnóstico, predicción de éxito, empleabilidad o decisiones de alto impacto.
- La lista exacta de campos **NO DEBE** fijarse hasta que exista revisión institucional/legal y una finalidad aprobada.

### Campos excluidos en este paquete

Este registro no contiene datos de participantes. En particular, **NO DEBE** incluir:

- respuestas reales, identificadores directos, datos de contacto, credenciales o secretos;
- contenido psicométrico no aprobado, claves, baremos o resultados individuales;
- una etiqueta clínica, de admisión, elegibilidad, éxito académico, empleabilidad o alto impacto;
- datos contextuales no justificados por una finalidad aprobada y minimizada.

Estas exclusiones describen el límite documental vigente; no sustituyen la política institucional/legal que debe definir el tratamiento futuro.

### Separación entre identidad y respuestas

La arquitectura candidata exige mantener la identidad restringida separada de respuestas, puntuaciones y resultados. En esta fase solo se documenta el principio: no existe implementación, almacenamiento ni control de acceso que pueda afirmarse como existente. La forma, custodio, acceso autorizado y trazabilidad **PENDIENTE DE REVISIÓN INSTITUCIONAL/LEGAL**.

### Retiro y solicitudes

- La persona debe poder conocer la ruta para retirar su participación, formular preguntas, pedir correcciones o presentar solicitudes cuando corresponda.
- El responsable, canal, verificación, alcance y efecto del retiro **PENDIENTES DE CONFIRMACIÓN**.
- No se inventa un correo, formulario, autoridad, plazo ni resultado de solicitud.

### Acceso

El acceso futuro **DEBERÍA** limitarse por función y necesidad, pero no se definen roles ni permisos concretos sin decisión institucional. **NO DEBE** suponerse que existe acceso autorizado, identidad institucional o capacidad operativa.

### Retención y eliminación

- La retención **DEBE** ser revisada antes de cualquier recolección; no se fija un plazo.
- La eliminación **DEBE** incluir una ruta verificable y condiciones aprobadas; no se fija un método ni una fecha.
- Estado de ambos puntos: **PENDIENTE DE REVISIÓN INSTITUCIONAL/LEGAL**.

## Ruta conceptual de solicitudes y datos

La siguiente ruta es una secuencia de investigación, no una arquitectura ni un flujo ejecutable:

1. **Fuente institucional autorizada:** catálogo y perfiles con versión, estado, vigencia y proveniencia; actualmente pendiente.
2. **Finalidad y población aprobadas:** consulta, comprensión, consentimiento/asentimiento y condiciones de acceso; actualmente pendientes.
3. **Tratamiento mínimo:** registrar solo lo que una revisión autorice; separar identidad de respuestas; actualmente pendiente.
4. **Análisis o puntuación versionada:** solo después de las puertas y evidencia correspondientes; no existe en este cambio.
5. **Salida exploratoria:** conjunto u orden plural con razones, incertidumbre, limitaciones y preguntas; no existe como producto.
6. **Solicitud, retiro, acceso, corrección o eliminación:** recibir por la ruta institucional que se confirme, verificar la solicitud, aplicar la decisión autorizada y conservar solo la evidencia mínima permitida; responsable, canal, plazos y procedimiento pendientes.
7. **Exportación de investigación:** solo si existe aprobación específica, minimización y control de acceso; no se crea ni se presume disponible.

## Dependencias y bloqueo

Este mapa depende de las consultas y decisiones registradas en [registros/descubrimiento.md](descubrimiento.md), [registros/decisiones.md](decisiones.md) y [registros/evidencia-faltante.md](evidencia-faltante.md). Mientras la revisión institucional/legal, el protocolo de menores y la ruta de solicitudes no estén confirmados, **NO DEBE** iniciarse recolección, publicación, implementación ni avance de puerta.
