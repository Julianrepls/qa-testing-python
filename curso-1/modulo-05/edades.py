"""Módulo 5 - misma función del módulo 4, ahora para practicar parametrize.

Clasifica una edad:
  - menor de 0        -> "no válida"
  - de 0 a 17         -> "menor"
  - de 18 a 64        -> "adulto"
  - de 65 en adelante -> "senior"
"""


def clasificar_edad(edad):
    if edad < 0:
        return "no válida"
    if edad < 18:
        return "menor"
    if edad < 65:
        return "adulto"
    return "senior"
