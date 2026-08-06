"""Tests del Módulo 5 - parametrize.

OBJETIVO: cubrir TODOS los casos de clasificar_edad con UN SOLO test
parametrizado. Debes incluir los 8 casos:
  - 3 caminos felices: 10->menor, 40->adulto, 80->senior
  - 5 casos límite:    0->menor, 17->menor, 18->adulto, 64->adulto, 65->senior
  - (el caso de error -1 lo dejamos para el mini-reto)
"""

import pytest
from edades import clasificar_edad


@pytest.mark.parametrize("edad, esperado", [
    (10, "menor"),
    (40, "adulto"),
    (80, "senior"),
    (0, "menor"),
    (17, "menor"),
    (70, "senior"),
    (18, "adulto"),
    (64, "adulto"),
    (65, "senior"),
    (-1, "no válida")
])
def test_clasificar_edad(edad, esperado):
    assert clasificar_edad(edad) == esperado
