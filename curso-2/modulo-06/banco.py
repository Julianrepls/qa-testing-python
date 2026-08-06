"""Curso 2 - Módulo 6. Operaciones de una cuenta bancaria.

Una cuenta es un dict: {"saldo": <numero>}.
"""


def depositar(cuenta, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    cuenta["saldo"] += cantidad
    return cuenta["saldo"]


def retirar(cuenta, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    if cantidad > cuenta["saldo"]:
        raise ValueError("Saldo insuficiente")
    cuenta["saldo"] -= cantidad
    return cuenta["saldo"]
