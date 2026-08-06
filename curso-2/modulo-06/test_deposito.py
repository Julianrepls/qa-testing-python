"""Tests de depósito. Usa la fixture 'cuenta' que vive en conftest.py.

Fíjate: NO importamos 'cuenta' de ningún sitio. pytest la inyecta sola
porque está definida en conftest.py.
"""

import pytest
from banco import depositar


def test_depositar_suma_al_saldo(cuenta):
    # cuenta viene de conftest.py con saldo 100
    nuevo_saldo = depositar(cuenta, 50)
    assert nuevo_saldo == 150


@pytest.mark.smoke
def test_depositar_devuelve_saldo_actualizado(cuenta):
    # Este test lo marcamos como 'smoke' (crítico / rápido)
    assert depositar(cuenta, 1) == 101