"""Módulo 7 - función con varios caminos para practicar cobertura.

Clasifica un precio:
  - precio negativo -> lanza ValueError
  - menos de 10     -> "barato"
  - de 10 a 49      -> "medio"
  - 50 o más        -> "caro"
"""


def categoria_precio(precio):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if precio < 10:
        return "barato"
    if precio < 50:
        return "medio"
    return "caro"
