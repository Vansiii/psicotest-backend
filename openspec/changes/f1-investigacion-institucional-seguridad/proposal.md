---
id: f1-investigacion-institucional-seguridad
title: "Fase 1 — Investigación institucional y límites de seguridad"
status: proposed
project_id: psicotest-backend
cross_repo_change_id: f1-investigacion-institucional-seguridad
related_project: psicotest-frontend
responsable: Marces
responsable_provisional: Marces
puertas_0_y_1: "NO APROBADAS"
estado_fase_producto: "NO INICIADA"
contrato: "El backend será propietario futuro del contrato de dominio/API; el frontend no puede inventarlo y solo lo consumirá cuando el backend lo publique y versione."
---

# Propuesta: Fase 1 — Investigación institucional y seguridad

## Intención

Documentar la investigación previa al software para validar orientación exploratoria, plural y de bajo riesgo. No aprueba puertas 0–1.

## Alcance

### Dentro
- Diferenciar secundaria, postulantes, otras personas interesadas y participantes de investigación; investigar consentimiento/asentimiento de menores y retiro.
- Definir, sujeto a revisión institucional/legal, minimización, acceso, retención, eliminación y solicitudes; estudiar accesibilidad, cultura, idioma, dispositivos y conectividad.
- Prohibir admisión automática, elegibilidad, éxito académico, empleabilidad, diagnóstico clínico y decisiones de alto impacto.
- Mantener TODA la oferta UAGRM. Escalonar por facultad/sitio es estrategia, no pre-filtro. Registrar [S29] (18 facultades/69 programas) vs [S30] (~80 repetidas), sin cifra oficial.
- Registrar riesgos, decisiones y evidencia faltante. El backend solo deja responsabilidades futuras: dominio, gobierno de datos, catálogo, puntuación y contrato API.

### Fuera
Fuera: código, API, infraestructura, autenticación, base de datos, tecnologías, catálogo reconciliado, instrumento, puntuación y datos. No modifica frontend ni autoriza implementación; no hay tareas de programación.

## Enfoque

Consultas, respuestas, decisiones y bloqueos; sin diseño técnico.

## Descubrimiento institucional

Áreas candidatas, responsables pendientes, sin nombres/cargos inventados: Orientación Vocacional (propósito/riesgo); facultades (cobertura); programas (fuentes); accesibilidad (barreras/acomodaciones); ética/investigación (revisión/menores); registros (poblaciones/solicitudes); tecnología (fuente/versionado); privacidad/legal (consentimiento, acceso, retención/eliminación). Registro: pregunta, respuesta, fuente/fecha, responsable, evidencia, decisión y bloqueo.

## Registros propuestos

- **Riesgos:** daño, población, impacto/probabilidad, mitigación, responsable, evidencia, estado y detención.
- **Decisiones:** qué decidir, quién decide, evidencia necesaria, dependencia, estado y bloqueo.
- **Datos:** minimización, finalidad, campos excluidos, separación identidad-respuestas, retiro, acceso, retención, eliminación y ruta; revisión legal pendiente.

## Capacidades

### Nuevas
- `investigacion-institucional-seguridad`: gobierno, poblaciones, datos, riesgos y límites de puertas 0–1.
### Modificadas
- Ninguna.

## Cierre medible

- [ ] **Puerta 0:** aprobación verificable de propósito, población, bajo riesgo, prohibiciones, consecuencias, privacidad, acceso, retención, eliminación y ausencia de ranking/corte/etiqueta definitiva.
- [ ] **Puerta 1:** responsables y rutas institucional, ética/investigación y privacidad confirmados; población, condiciones, cobertura/recomendación, accesibilidad, salvaguardas de menores y generalización aprobadas.
- [ ] Cada decisión crítica tiene responsable, protocolo y evidencia enlazable. Sin respuesta: bloqueo; no se infiere aprobación ni se avanza.

## Áreas afectadas

- `openspec/changes/f1-investigacion-institucional-seguridad/`: documentación.
- Backend futuro: propietario del contrato; frontend consumidor tras publicación/versionado.

## Riesgos

Riesgos: falsa sensación de avance, autoridades/cifras inventadas y decisiones prematuras sobre menores/datos. Mitigar con `proposed`, pendientes, revisión y detención.

## Plan de reversión

Retirar/actualizar con historial, invalidar dependencias y mantener software sin cambios.

## Dependencias

Respuestas UAGRM, responsables, protocolos y evidencia de puertas 0–1.
