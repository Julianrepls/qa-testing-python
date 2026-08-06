"""Módulo 4 - función para practicar el diseño de casos de prueba.

Clasifica una edad en una categoría:
  - menor de 0       -> "no válida"
  - de 0 a 17        -> "menor"
  - de 18 a 64       -> "adulto"
  - de 65 en adelante-> "senior"
"""


def clasificar_edad(edad):
    if edad < 0:
        return "no válida"
    if edad < 18:
        return "menor"
    if edad < 65:
        return "adulto"
    return "senior"
