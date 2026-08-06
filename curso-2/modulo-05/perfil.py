"""Curso 2 - Módulo 5. Cliente de API que devuelve el perfil de un usuario.

La app espera que la API devuelva un JSON con este CONTRATO:
  - nombre: str
  - edad:   int
  - activo: bool
"""

import requests


def obtener_perfil(user_id):
    respuesta = requests.get(f"https://api.ejemplo.com/users/{user_id}")
    respuesta.raise_for_status()
    return respuesta.json()
