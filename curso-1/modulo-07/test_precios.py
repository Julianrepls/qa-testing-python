"""Tests del Módulo 7 - cobertura.

De momento SOLO probamos 2 de los 4 caminos, a propósito,
para ver cómo la cobertura nos avisa de lo que falta.
"""

from precios import categoria_precio
import pytest


def test_precio_barato():
    assert categoria_precio(5) == "barato"


def test_precio_medio():
    assert categoria_precio(20) == "medio"

def test_precio_caro():
    assert categoria_precio(100) == "caro"

def test_precio_negativo():
    with pytest.raises(ValueError):
        categoria_precio(-3)

def test_precio_frontera_medio():
    assert categoria_precio(45) == "medio"