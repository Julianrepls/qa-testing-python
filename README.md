# 🧪 QA Testing con Python — Mi ruta de aprendizaje

Repositorio donde documento mi progreso aprendiendo **QA Testing / Test Automation con Python**, desde los fundamentos hasta técnicas intermedias usadas en equipos reales. Cada módulo incluye código de ejemplo y sus tests, escritos y ejecutados paso a paso.

> Objetivo: desarrollar una base sólida como **QA Automation Engineer**.

## 🛠️ Tecnologías y herramientas

- **Python 3.12**
- **pytest** — framework de testing (fixtures, `parametrize`, markers, `conftest.py`)
- **pytest-cov** — cobertura de código
- **unittest.mock** — mocking de dependencias (`patch`, `return_value`, `side_effect`)
- **requests** — testing de clientes de API REST
- **Playwright** — testing end-to-end (E2E) de interfaz
- **GitHub Actions** — integración continua (CI)

## 📚 Contenido

### Curso 1 — Fundamentos ([`curso-1/`](curso-1/))
Qué es QA (QA/QC/Testing), tipos de prueba y pirámide de testing, estructura AAA,
diseño de casos de prueba (valores límite), `parametrize` y fixtures, testing de
excepciones, cobertura de código, testing de integración, bug reports, introducción
a E2E con Playwright y buenas prácticas.

### Curso 2 — Intermedio ([`curso-2/`](curso-2/))
Mocking en profundidad (`patch`, `return_value`, `side_effect`), mockeo de tiempo y
aleatoriedad, testing de APIs REST mockeando la red, validación de contratos de API,
organización profesional de suites (`conftest.py`, markers, `pytest.ini`) e
integración continua con GitHub Actions.

## ▶️ Cómo ejecutar los tests

```bash
# Instalar dependencias
pip install pytest pytest-cov requests

# Ejecutar los tests de un módulo
cd curso-2/modulo-01
pytest -v

# Con reporte de cobertura
pytest --cov=. --cov-report=term-missing
```

---

*Repositorio de aprendizaje en progreso. Cada módulo refleja un concepto nuevo de QA aplicado de forma práctica.*
