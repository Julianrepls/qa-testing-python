"""Curso 2 - Módulo 2. Código bajo prueba.

precio_con_iva pide el precio base al servicio externo y le suma el 21% de IVA.
Si el servicio falla, propaga un error controlado.
"""

import precios_api


def precio_con_iva(producto_id):
    base = precios_api.obtener_precio_base(producto_id)
    return round(base * 1.21, 2)
