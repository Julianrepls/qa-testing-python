"""Módulo 8 - mini-sistema de pedidos para practicar testing de integración.

Tres piezas que colaboran:
  1) validar_carrito  -> comprueba que el carrito no está vacío
  2) calcular_subtotal -> suma los precios de los productos
  3) aplicar_impuesto  -> añade un 21% de IVA al subtotal

Y una función que las une todas: procesar_pedido.
"""


def validar_carrito(carrito):
    """Lanza ValueError si el carrito está vacío."""
    if len(carrito) == 0:
        raise ValueError("El carrito está vacío")
    return True


def calcular_subtotal(carrito):
    """Suma los precios de todos los productos del carrito."""
    return sum(producto["precio"] for producto in carrito)


def aplicar_impuesto(subtotal):
    """Añade un 21% de IVA y redondea a 2 decimales."""
    return round(subtotal * 1.21, 2)


def procesar_pedido(carrito):
    """Flujo completo: valida, calcula el subtotal y aplica el impuesto."""
    validar_carrito(carrito)
    subtotal = calcular_subtotal(carrito)
    total = aplicar_impuesto(subtotal)
    return total
