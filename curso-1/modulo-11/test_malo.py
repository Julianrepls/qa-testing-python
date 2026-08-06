"""Módulo 11 - RETO: audita este test.

Este test 'pasa' en verde, pero rompe VARIAS de las 6 reglas de oro
de un buen test. Tu tarea es encontrar los problemas (no arreglarlo aún).
"""

import datetime
from edades import clasificar_edad


saldo_acumulado = 0


def test_1():
    global saldo_acumulado

    # comprueba varias cosas distintas de golpe
    assert clasificar_edad(10) == "menor"
    assert clasificar_edad(40) == "adulto"
    assert clasificar_edad(80) == "senior"

    # usa la fecha de hoy para decidir qué espera
    hoy = datetime.date.today()
    if hoy.weekday() < 5:
        assert clasificar_edad(20) == "adulto"

    # depende de una variable global que otros tests podrían cambiar
    saldo_acumulado = saldo_acumulado + 1
    assert saldo_acumulado == 1
