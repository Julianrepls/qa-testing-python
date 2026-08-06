"""Tests del Módulo 6 - probar excepciones con pytest.raises.

OBJETIVO:
  1) test normal: una edad válida sigue devolviendo su categoría.
  2) test de excepción: una edad negativa debe LANZAR ValueError.
"""

import pytest
from edades import clasificar_edad


def test_edad_valida_devuelve_categoria():
    # Un caso normal sigue funcionando como siempre
    assert clasificar_edad(30) == "adulto"


def test_edad_negativa_lanza_error():
    with pytest.raises(ValueError):
        clasificar_edad(-5)

def test_edad_negativa_lanza_error_con_mensaje():
    with pytest.raises(ValueError, match="negativa"):
        clasificar_edad(-10)
    
