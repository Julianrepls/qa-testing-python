# 🧪 QA Testing con Python — Mi ruta de aprendizaje

[![Tests](https://github.com/Julianrepls/qa-testing-python/actions/workflows/tests.yml/badge.svg)](https://github.com/Julianrepls/qa-testing-python/actions/workflows/tests.yml)

Repositorio donde documento mi progreso aprendiendo **QA Testing / Test Automation con Python**, desde los fundamentos hasta técnicas intermedias usadas en equipos reales. Cada módulo incluye código de ejemplo y sus tests, escritos y ejecutados paso a paso.

> Objetivo: desarrollar una base sólida como **QA Automation Engineer**.

**22 módulos** repartidos en dos cursos. Los tests de cada módulo se ejecutan automáticamente en GitHub Actions con cada push.

## 🛠️ Tecnologías y herramientas

- **Python 3.12**
- **pytest** — framework de testing (fixtures, `parametrize`, markers, `conftest.py`, `pytest.ini`)
- **pytest-cov** — cobertura de código
- **unittest.mock** — mocking de dependencias (`patch`, `return_value`, `side_effect`)
- **requests** — testing de clientes de API REST
- **Playwright** — testing end-to-end (E2E) de interfaz, con Page Object Model
- **SQLite** — validación de datos en base de datos
- **pytest-bdd** — BDD con Gherkin (`Given` / `When` / `Then`)
- **Locust** — testing de rendimiento
- **GitHub Actions** — integración continua (CI)

## 📚 Contenido

### Curso 1 — Fundamentos ([`curso-1/`](curso-1/))

| Módulo | Tema |
|---|---|
| [01](curso-1/modulo-01/) | Qué es QA: diferencia entre QA, QC y Testing |
| [02](curso-1/modulo-02/) | Tipos de prueba y pirámide de testing |
| [03](curso-1/modulo-03/) | Primer test con pytest y estructura AAA (Arrange-Act-Assert) |
| [04](curso-1/modulo-04/) | Diseño de casos: caminos felices, valores límite y casos de error |
| [05](curso-1/modulo-05/) | Buenos asserts, fixtures y `@pytest.mark.parametrize` |
| [06](curso-1/modulo-06/) | Testing de excepciones con `pytest.raises` |
| [07](curso-1/modulo-07/) | Cobertura de código: cómo medirla y cómo leer el reporte |
| [08](curso-1/modulo-08/) | Testing de integración |
| [09](curso-1/modulo-09/) | Testing manual vs automatizado y cómo documentar un [bug report](curso-1/modulo-09/bug_report.md) |
| [10](curso-1/modulo-10/) | Introducción a E2E / UI con Playwright |
| [11](curso-1/modulo-11/) | Buenas prácticas: auditar un test que pasa en verde pero está mal escrito |

### Curso 2 — Intermedio ([`curso-2/`](curso-2/))

| Módulo | Tema |
|---|---|
| [01](curso-2/modulo-01/) | Mocking: qué es un mock y por qué aislar dependencias (`patch`) |
| [02](curso-2/modulo-02/) | `return_value`, `side_effect` y verificar llamadas (`assert_called_once_with`) |
| [03](curso-2/modulo-03/) | Mockear lo incontrolable: tiempo, aleatoriedad y errores de red |
| [04](curso-2/modulo-04/) | Testing de código que llama a una API REST, mockeando la red |
| [05](curso-2/modulo-05/) | Validar respuestas: status codes, JSON y contrato/esquema |
| [06](curso-2/modulo-06/) | Estructura profesional: `conftest.py`, fixtures compartidas, markers, `pytest.ini` |
| [07](curso-2/modulo-07/) | CI con GitHub Actions: que los tests corran solos en cada push |
| [08](curso-2/modulo-08/) | Playwright avanzado: [Page Object Model](curso-2/modulo-08/login_page.py) y esperas robustas |
| [09](curso-2/modulo-09/) | SQL para QA: validar datos en base de datos (SQLite) |
| [10](curso-2/modulo-10/) | BDD con `pytest-bdd` y Gherkin ([`.feature`](curso-2/modulo-10/suma.feature)) |
| [11](curso-2/modulo-11/) | Testing de rendimiento con [Locust](curso-2/modulo-11/locustfile.py) |

## ▶️ Cómo ejecutar los tests

```bash
# Instalar dependencias
pip install -r requirements-dev.txt

# Navegadores para los tests E2E (módulos 1-10 y 2-08)
playwright install chromium
```

Cada módulo es un mini-proyecto independiente, así que los tests se ejecutan
desde dentro de su carpeta:

```bash
cd curso-2/modulo-01
pytest -v
```

Con reporte de cobertura:

```bash
pytest --cov=. --cov-report=term-missing
```

## 🔄 Integración continua

El workflow [`.github/workflows/tests.yml`](.github/workflows/tests.yml) recorre
cada módulo y ejecuta su suite por separado. Acumula los fallos, de modo que un
módulo roto no oculta el resultado del resto.

---

*Repositorio de aprendizaje en progreso. Cada módulo refleja un concepto nuevo de QA aplicado de forma práctica.*
