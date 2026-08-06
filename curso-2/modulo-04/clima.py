"""Curso 2 - Módulo 4. Cliente de una API REST del tiempo.

obtener_temperatura llama a una API externa y devuelve la temperatura de una
ciudad. Si la API responde con un código distinto de 200, lanza un error.
"""

import requests


def obtener_temperatura(ciudad):
    respuesta = requests.get(f"https://api.clima.com/actual?ciudad={ciudad}")

    if respuesta.status_code != 200:
        raise RuntimeError(f"Error al consultar el clima: {respuesta.status_code}")

    datos = respuesta.json()
    return datos["temperatura"]
