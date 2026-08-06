"""Tests del Curso 2 - Módulo 4: testing de una API mockeando requests.

TAREA 1 (test_obtener_temperatura_ok):
  Simula una respuesta 200 con JSON {"temperatura": 25} y comprueba
  que obtener_temperatura("Madrid") devuelve 25.

TAREA 2 (test_obtener_temperatura_error_404): la harás en el mini-reto.
"""

from unittest.mock import patch, Mock
import clima
import pytest

#vamos a hacer aqui el primer test, que es el que nos piden en la tarea 1.(camino feliz sin errores)
@patch("clima.requests.get")
def test_obtener_temperatura_ok(mock_get):
    #   TODO:
    #   1) crea una respuesta falsa:  respuesta = Mock()
    #   2) respuesta.status_code = 200
    #   3) respuesta.json.return_value = {"temperatura": 25}
    #   4) mock_get.return_value = respuesta
    #   5) comprueba que clima.obtener_temperatura("Madrid") == 25
  respuesta = Mock()
  respuesta.status_code = 200
  respuesta.json.return_value = {"temperatura": 25}
  mock_get.return_value = respuesta
  assert clima.obtener_temperatura("Madrid") == 25

#vamos a hacer a la otra tarea (un caso que el test falle) para ver cómo se hace un test de error.
@patch("clima.requests.get")
def test_obtener_temperatura_error_404(mock_get):
    respuesta = Mock()
    respuesta.status_code = 404
    mock_get.return_value = respuesta
    with pytest.raises(RuntimeError):
        clima.obtener_temperatura("Madrid")