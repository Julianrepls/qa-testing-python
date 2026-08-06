"""Aquí escribes TÚ tu primer test.

Reglas básicas de pytest:
- El archivo debe empezar por  test_
- La función de test debe empezar por  test_
- Dentro usas  assert  para comprobar que algo es verdad.

OBJETIVO: escribe un test que compruebe que sumar(2, 3) devuelve 5.
"""

from calculadora import sumar, sumar_negativos


def test_sumar():
    # TODO: escribe aquí tu comprobación con assert
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    # TODO: escribe aquí tu comprobación con assert
    assert sumar_negativos(-2, -3) == -5