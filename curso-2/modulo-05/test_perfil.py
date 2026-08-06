"""Tests del Curso 2 - Módulo 5: validar el CONTRATO de la respuesta.

TAREA 1 (test_perfil_tiene_contrato_correcto):
  Simula una respuesta con {"nombre": "Ana", "edad": 30, "activo": True}
  y comprueba que:
    - existen los campos "nombre", "edad" y "activo"
    - "nombre" es str, "edad" es int, "activo" es bool

TAREA 2 (mini-reto): detectar un contrato ROTO.
"""

from unittest.mock import patch, Mock
import perfil
import pytest

@patch("perfil.requests.get")
def test_perfil_tiene_contrato_correcto(mock_get):
    # Arrange: respuesta falsa que cumple el contrato
    respuesta = Mock()
    respuesta.json.return_value = {"nombre": "Ana", "edad": 30, "activo": True}
    mock_get.return_value = respuesta

    # Act
    datos = perfil.obtener_perfil(1)

    # Assert: comprueba EXISTENCIA de campos y TIPOS
    assert "nombre" in datos
    assert "edad" in datos
    assert "activo" in datos
    assert isinstance(datos["nombre"], str)
    assert isinstance(datos["edad"], int)
    assert isinstance(datos["activo"], bool)



# De esta manera no estamos comprobando *qué* valores tiene el usuario, sino que la respuesta **tiene la forma correcta**: 
# los tres campos existen y son del tipo esperado.


# Este test seguiría en verde aunque Ana se llamara "Juan" o tuviera 50 años 
# (el dato cambia), pero **saltaría en rojo** si la API dejara de mandar `edad` o la enviara como texto "30".
# Es decir, vigilamos justo lo que debe: **la estructura**, no el contenido.


@patch("perfil.requests.get")
def test_perfil_tiene_contrato_roto_edad(mock_get):
    # Arrange: respuesta falsa que cumple el contrato
    respuesta = Mock()
    respuesta.json.return_value = {"nombre": "Ana", "edad": "30", "activo": True}
    mock_get.return_value = respuesta
  # Act
    datos = perfil.obtener_perfil(1)
  #assert: comprueba EXISTENCIA de campos y TIPOS
    assert "nombre" in datos
    assert "edad" in datos
    assert "activo" in datos
    assert isinstance(datos["nombre"], str)
    assert not isinstance(datos["edad"], int)
    assert isinstance(datos["activo"], bool)