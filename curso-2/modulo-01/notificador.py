"""Curso 2 - Módulo 1. Dependencia 'externa' que NO queremos ejecutar en tests.

Imagina que esta función se conecta a un servidor SMTP real y envía un email.
Es lenta, externa y con efectos secundarios: el candidato perfecto para mockear.
"""


def enviar_bienvenida(email):
    # En la vida real: conexión SMTP, envío real, etc.
    print(f"[SMTP] Enviando email de bienvenida a {email}...")
    return True
