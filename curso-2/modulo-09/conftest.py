"""Fixtures compartidas del Módulo 9.

La fixture 'conn' crea una base de datos SQLite EN MEMORIA, fresca para cada
test, y la cierra al terminar (setup + teardown con yield).
"""

import sqlite3
import pytest
from db import crear_tabla


@pytest.fixture
def conn():
    conexion = sqlite3.connect(":memory:")  # SETUP: BD nueva en memoria
    crear_tabla(conexion)
    yield conexion                          # aquí corre el test
    conexion.close()                        # TEARDOWN: limpiar al acabar
