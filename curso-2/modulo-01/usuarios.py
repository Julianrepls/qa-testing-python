"""Curso 2 - Módulo 1. Nuestro código bajo prueba.

registrar_usuario valida el email, y si es válido, dispara el email de
bienvenida a través del módulo notificador (la dependencia externa).
"""

import notificador


def registrar_usuario(email):
    if "@" not in email:
        raise ValueError("Email inválido")

    notificador.enviar_bienvenida(email)

    return {"email": email, "activo": True}
