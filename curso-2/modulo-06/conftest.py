"""conftest.py - fixtures compartidas por TODOS los tests de esta carpeta.

pytest detecta este archivo automáticamente. No hay que importarlo.
Cualquier test puede usar la fixture 'cuenta' con solo pedirla por su nombre.
"""

import pytest


@pytest.fixture
def cuenta():
    """Una cuenta nueva con 100 de saldo, fresca para cada test."""
    return {"saldo": 100}
