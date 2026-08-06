"""Curso 2 - Módulo 3. Código que depende del RELOJ (difícil de testear tal cual).

saludo() devuelve un saludo según la hora actual:
  - antes de las 12  -> "Buenos días"
  - de 12 a 19       -> "Buenas tardes"
  - de 20 en adelante-> "Buenas noches"
"""

from datetime import datetime


def saludo():
    hora = datetime.now().hour
    if hora < 12:
        return "Buenos días"
    if hora < 20:
        return "Buenas tardes"
    return "Buenas noches"
