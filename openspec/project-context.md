# Contexto del proyecto: psicotest-backend

## Identidad

TestPsico es una iniciativa de investigación para orientación vocacional/educativa exploratoria y de bajo riesgo sobre carreras y programas autorizados de toda la UAGRM. La salida futura debe ser plural o un orden exploratorio de afinidades, razones, incertidumbre, limitaciones y preguntas de siguiente paso. No debe afirmar una carrera correcta, admisión, elegibilidad, éxito académico, empleabilidad, diagnóstico clínico ni una decisión de alto impacto.

Este repositorio está vacío y no tiene fases de implementación iniciadas. El backend será propietario futuro del dominio, catálogo, perfiles educativos, evaluación, puntuación, afinidades, recomendaciones y contrato API; el frontend será consumidor futuro del contrato publicado.

## Stack y arquitectura propuestos como contexto

Los documentos proponen evaluar Python con un marco HTTP y validación de esquemas para el backend, PostgreSQL u otra base relacional, almacenamiento de objetos si fuera necesario, un proveedor institucional de identidad y R/Python u otra herramienta reproducible para análisis. No se seleccionó ninguna tecnología.

La arquitectura candidata separa catálogo institucional, `program_profile`, evaluación, puntuación, motor de afinidades, reporte, auditoría y exportación de investigación aprobada. El backend debe controlar contratos, reglas versionadas, autorización y trazabilidad. Estas son hipótesis sujetas a investigación, gobernanza, seguridad, mantenimiento y autorización; no capacidades existentes.

## Convenciones y límites

- OpenSpec en este repositorio es la única fuente compartida y versionada de artefactos SDD.
- Los artefactos se redactan en español neutral y profesional.
- La ejecución es interactiva, con preferencia `ask-always` para la entrega y presupuesto de revisión de 400 líneas.
- Facultad, sitio, nivel, modalidad y disponibilidad son metadatos o filtros explícitos; no son pre-filtros obligatorios de recomendación.
- No deben inventarse datos de catálogo, perfiles, ítems, baremos, roles, API, comandos, pruebas, infraestructura o contratos.
- No deben incluirse respuestas reales, datos identificables, credenciales ni contenido psicométrico no aprobado.

## Estado de pruebas y calidad

No existen `package.json`, `go.mod`, `pyproject.toml`, `Cargo.toml`, `requirements.txt`, proyectos .NET, configuración CI, código fuente, tests, runner, cobertura, linter, type checker, formatter ni infraestructura detectables. Por tanto, `strict_tdd: false`: no hay runner de pruebas disponible para habilitar TDD estricto.

## Decisiones pendientes

- Aprobación institucional del propósito, población, salvaguardas y nivel de consecuencias.
- Reconciliación de un catálogo UAGRM autorizado, versionado y con IDs estables.
- Constructos, matriz de especificación, contenido original, puntuación y evidencia psicométrica.
- Modalidad, idioma, accesibilidad, procedimiento para menores y jóvenes, privacidad y retención.
- Forma exacta de salida plural, incertidumbre, empates y preguntas de exploración.
- Lenguaje/marco backend, persistencia, identidad, permisos, operación, infraestructura y estrategia de pruebas.
- Contrato API backend/frontend, compatibilidad, monitoreo, revalidación y pausa.
- Identidad local futura de Engram; no forma parte del almacén normativo de este proyecto.
