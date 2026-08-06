"""Módulo 3 - ejemplo para practicar la estructura AAA.

Cada producto es un diccionario con 'nombre' y 'stock'.
"""


def filtrar_disponibles(productos):
    """Devuelve solo los productos que tienen stock mayor que 0."""
    return [p for p in productos if p["stock"] > 0]
