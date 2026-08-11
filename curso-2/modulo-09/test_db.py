"""Tests del Curso 2 - Módulo 9: validar datos en base de datos.

La fixture 'conn' (en conftest.py) te da una BD SQLite en memoria con la
tabla 'usuarios' ya creada.

TAREA 1 (test_insertar_incrementa_conteo):
  Inserta un usuario y comprueba que ahora hay 1 usuario en la BD.

TAREA 2 (mini-reto): buscar por email.
"""

from db import insertar_usuario, contar_usuarios, buscar_por_email


def test_insertar_incrementa_conteo(conn):
    # Al principio la BD está vacía
    assert contar_usuarios(conn) == 0

    # Insertamos un usuario
    insertar_usuario(conn, "Alice", "alice@mail.com")
    # Comprobamos que ahora hay 1 usuario
    assert contar_usuarios(conn) == 1

def test_buscar_por_email(conn):
    # Insertamos un usuario
    insertar_usuario(conn, "Alice", "alice@mail.com")
    
    # Comprobamos que podemos buscarlo por email
    assert buscar_por_email(conn, "alice@mail.com") == "Alice"

def test_buscar_usuario_no_existe(conn): 
    # Comprobamos que buscar un email que no existe devuelve None
    assert buscar_por_email(conn, "nadie@mail.com") is None