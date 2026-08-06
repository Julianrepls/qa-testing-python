"""Tests del Módulo 3 - practica la estructura AAA.

OBJETIVO: escribe un test para filtrar_disponibles usando las 3 fases:
  Arrange -> prepara una lista con 3 productos (uno con stock 0)
  Act     -> llama a filtrar_disponibles
  Assert  -> comprueba que devuelve solo los 2 que tienen stock
"""

from inventario import filtrar_disponibles


def test_filtrar_disponibles():
    # Arrange
    productos = [
      {"nombre": "cuchara", "stock": 3}, 
      {"nombre": "tenedor", "stock": 1}, 
      {"nombre": "plato", "stock": 0}
    ]

    # Act
    resultado = filtrar_disponibles(productos)

    # Assert
    assert len(resultado) == 2

def test_filtrar_excluye_sin_stock():
    # Arrange
    productos = [
      {"nombre": "cuchara", "stock": 3}, 
      {"nombre": "tenedor", "stock": 1}, 
      {"nombre": "plato", "stock": 0}
    ]

    # Act
    resultado = filtrar_disponibles(productos)

    # Assert
    assert all(p["stock"] < 0 for p in resultado)

def test_filtrar_excluye_sin_stock():
    # Arrange
    productos = [
        {"nombre": "cuchara", "stock": 3},
        {"nombre": "plato", "stock": 0},
    ]

    # Act
    resultado = filtrar_disponibles(productos)

    # Assert
    assert resultado == [{"nombre": "cuchara", "stock": 3}]