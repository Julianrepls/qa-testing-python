"""Módulo 2 - mini-proyecto 'tienda' para hablar de tipos de prueba."""


def calcular_subtotal(precios):
    """Suma una lista de precios y devuelve el subtotal."""
    return sum(precios)


def aplicar_descuento(subtotal, porcentaje):
    """Aplica un descuento (en %) al subtotal y devuelve el total final."""
    descuento = subtotal * porcentaje / 100
    return subtotal - descuento
