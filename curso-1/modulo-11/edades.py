"""Módulo 11 - código bajo prueba para el reto de auditoría.

Copia de la versión del módulo 6: clasificar_edad LANZA un ValueError con
edades negativas en lugar de devolver "no válida".

El test que lo acompaña (test_malo.py) pasa en verde a propósito, pese a
romper varias reglas de un buen test. Encontrar esos problemas es el reto.
"""


def clasificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 18:
        return "menor"
    if edad < 65:
        return "adulto"
    return "senior"
