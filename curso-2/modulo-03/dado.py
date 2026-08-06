"""Curso 2 - Módulo 3 (mini-reto). Código que depende del AZAR."""

import random


def tirar_dado():
    """Devuelve un número aleatorio del 1 al 6."""
    return random.randint(1, 6)


def es_seis():
    """Tira el dado y devuelve True si salió un 6."""
    return tirar_dado() == 6
