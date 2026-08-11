# Plan de Aprendizaje — Curso 2: QA Testing Intermedio/Avanzado con Python

Continuación del Curso 1 (11 módulos, completado). Nivel: intermedio, ejercicios
más realistas. Mismo método: concepto breve + ejemplo, TÚ escribes el test,
corrijo y ejecutamos (verde/rojo), mini-reto y cuestionario. No avanzamos hasta
confirmar que entendiste. 30 min/día.

## Bloque A — Tests robustos y aislados (Mocking)
- **Módulo 1**: Mocking — qué es un mock y por qué aislar dependencias. `unittest.mock` + `patch`. ← EMPEZAMOS AQUÍ
- **Módulo 2**: `return_value`, `side_effect` y verificar llamadas (`assert_called_once_with`).
- **Módulo 3**: Mockear lo incontrolable — tiempo, aleatoriedad y errores de red.

## Bloque B — Testing de APIs
- **Módulo 4**: Testing de código que llama a una API REST (`requests`), mockeando la red.
- **Módulo 5**: Validar respuestas: status codes, JSON y contrato/esquema.

## Bloque C — Organización profesional y CI
- **Módulo 6**: Estructura de proyecto de tests: `conftest.py`, fixtures compartidas, markers, `pytest.ini`.
- **Módulo 7**: CI con GitHub Actions — que los tests corran solos en cada push. Git para tu portfolio.

## Bloque D — E2E avanzado y datos
- **Módulo 8**: Playwright avanzado — Page Object Model, esperas robustas, fixtures propias.
- **Módulo 9**: SQL para QA — validar datos en base de datos (SQLite).

## Bloque E — Metodologías y cierre
- **Módulo 10**: BDD con `pytest-bdd` (Gherkin: Given/When/Then).
- **Módulo 11**: Testing de rendimiento (Locust) + cierre y siguientes pasos.

---
Progreso: [x] M1 · [x] M2 · [x] M3 · [x] M4 · [x] M5 · [x] M6 · [x] M7 · [x] M8 · [x] M9 · [ ] M10 · [ ] M11
