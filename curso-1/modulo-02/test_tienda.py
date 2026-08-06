"""Tests del Módulo 2.

OBJETIVO: escribe un test UNITARIO para calcular_subtotal.
Comprueba que calcular_subtotal([10, 20, 30]) devuelve 60.
"""

from tienda import calcular_subtotal, aplicar_descuento


def test_subtotal_con_descuento():
    subtotal = calcular_subtotal([10, 20, 30])
    total = aplicar_descuento(subtotal, 10)
    assert total == 54  # 60 - 10% = 54
