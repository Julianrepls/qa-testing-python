"""Tests del Módulo 5 (parte 2) - fixtures.

OBJETIVO: usar UNA fixture 'productos' compartida por dos tests.
"""

import pytest
from inventario import contar_productos, hay_agotados


@pytest.fixture
def productos():
    """El 'Arrange' compartido: una lista de productos de ejemplo."""
    return [
        {"nombre": "camiseta", "stock": 5},
        {"nombre": "pantalon", "stock": 3},
        {"nombre": "agotado", "stock": 0},
    ]


def test_contar(productos):
    # Act + Assert: hay 3 productos en la fixture
    assert contar_productos(productos) == 3


def test_hay_agotados(productos):
    assert hay_agotados(productos)
