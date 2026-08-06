"""Tests del Módulo 4 - diseño de casos de prueba.

Vamos a cubrir las 3 categorías:
  - Camino feliz: una edad normal de cada categoría
  - Casos límite: las edades frontera (0, 17, 18, 64, 65)
  - Caso de error: una edad inválida (negativa)

Escribiremos los tests paso a paso siguiendo las instrucciones del mentor.
"""

from edades import clasificar_edad


# Empezaremos por aquí en la práctica guiada.
def test_clasificar_17_es_menor():
    # Arrange
    edad = 17
    # Act
    resultado = clasificar_edad(edad)
    # Assert
    assert resultado == "menor"

def test_clasificar_18_es_adulto():
    # Arrange
    edad = 18
    # Act
    resultado = clasificar_edad(edad)
    # Assert
    assert resultado == "adulto"

def test_clasificar_65_es_senior():
    # Arrange
    edad = 65
    # Act
    resultado = clasificar_edad(edad)
    # Assert
    assert resultado == "senior"

def test_clasificar_edad_negativa_es_no_valida():
    # Arrange
    edad = -1
    # Act
    resultado = clasificar_edad(edad)
    # Assert
    assert resultado == "no válida"