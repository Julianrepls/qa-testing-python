"""Módulo 5 (parte 2) - funciones de inventario para practicar fixtures."""


def contar_productos(productos):
    """Devuelve cuántos productos hay en la lista."""
    return len(productos)


def hay_agotados(productos):
    """Devuelve True si algún producto tiene stock 0."""
    return any(p["stock"] == 0 for p in productos)
