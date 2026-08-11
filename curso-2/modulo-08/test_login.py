"""Tests del Curso 2 - Módulo 8: Playwright con Page Object Model.

'page' es la fixture de pytest-playwright. Usamos la clase LoginPage
para interactuar con la web, sin tocar selectores en el test.

TAREA 1 (test_login_correcto):
  Carga la página, haz login con admin/1234 y comprueba que el mensaje
  es "Bienvenido, admin".

TAREA 2 (test_login_incorrecto): en el mini-reto.
"""

from pathlib import Path
from login_page import LoginPage

URL = (Path(__file__).parent / "index.html").as_uri()


def test_login_correcto(page):
    login = LoginPage(page)
    login.cargar(URL)
    login.login("admin", "1234")
    assert login.obtener_mensaje() == "Bienvenido, admin"

def test_login_incorrecto(page):
    login = LoginPage(page)
    login.cargar(URL)
    login.login("hacker", "0000")
    assert login.obtener_mensaje() == "Credenciales incorrectas"
