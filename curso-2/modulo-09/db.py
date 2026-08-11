"""Curso 2 - Módulo 9. Operaciones sobre una base de datos SQLite de usuarios.

Usamos sqlite3 (incluido en Python). Recibimos la conexión como parámetro
para poder testear con una BD en memoria.
"""


def crear_tabla(conn):
    conn.execute(
        "CREATE TABLE usuarios ("
        "id INTEGER PRIMARY KEY, "
        "nombre TEXT, "
        "email TEXT UNIQUE)"
    )
    conn.commit()


def insertar_usuario(conn, nombre, email):
    conn.execute(
        "INSERT INTO usuarios (nombre, email) VALUES (?, ?)",
        (nombre, email),
    )
    conn.commit()


def contar_usuarios(conn):
    cursor = conn.execute("SELECT COUNT(*) FROM usuarios")
    return cursor.fetchone()[0]


def buscar_por_email(conn, email):
    cursor = conn.execute(
        "SELECT nombre FROM usuarios WHERE email = ?", (email,)
    )
    fila = cursor.fetchone()
    return fila[0] if fila else None
