"""Módulo 9 - función con un bug para practicar el bug report.

Regla de negocio (lo que DEBERÍA hacer):
  El cupón "DESCUENTO10" aplica un 10% de descuento sobre el precio.
  Ejemplo: precio 200 con "DESCUENTO10" -> 180 (le quitas el 10%).
  Cualquier otro cupón no cambia el precio.
"""


def aplicar_cupon(precio, cupon):
    if cupon == "DESCUENTO10":
        return precio - 10
    return precio
