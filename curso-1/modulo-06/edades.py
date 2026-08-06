"""Módulo 6 - versión de clasificar_edad que LANZA un error con edades inválidas.

A diferencia del módulo 4/5, ahora una edad negativa no devuelve "no válida":
levanta (raise) una excepción ValueError para avisar de que el dato es inválido.
"""


def clasificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 18:
        return "menor"
    if edad < 65:
        return "adulto"
    return "senior"
