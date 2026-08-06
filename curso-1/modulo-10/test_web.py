"""Módulo 10 - test E2E con Playwright contra una web LOCAL.

'page' es una fixture de pytest-playwright: una pestaña del navegador.
Probamos nuestro propio index.html (no necesita internet).
"""

from pathlib import Path

# Construye la URL del archivo local: file:///C:/.../index.html
URL = (Path(__file__).parent / "index.html").as_uri()


def test_titulo_de_la_web(page):
    # Act: el navegador abre nuestra web local
    page.goto(URL)

    # Assert: el título de la pestaña contiene "Tienda QA"
    assert "Tienda QA" in page.title()


def test_encabezado_de_la_web(page):
    page.goto(URL)

    # Assert: el <h1> (id="titulo") muestra el texto de bienvenida
    encabezado = page.locator("#titulo").inner_text()
    assert encabezado == "Bienvenido a la Tienda QA"


def test_boton_comprar(page):
    page.goto(URL)

    # Al principio el mensaje está vacío
    assert page.locator("#mensaje").inner_text() == ""
    # Act: hacemos click en el botón de comprar
    page.click("#boton-comprar")
    # Estado final: el mensaje muestra "¡Compra realizada con éxito!"
    assert page.locator("#mensaje").inner_text() == "¡Compra realizada con éxito!"

