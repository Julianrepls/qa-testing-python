"""Curso 2 - Módulo 2. Dependencia externa: un servicio de precios.

obtener_precio_base simula una llamada a un servicio externo (lento/inestable).
No queremos ejecutarlo de verdad en los tests: lo mockearemos.
"""


def obtener_precio_base(producto_id):
    # En la vida real: llamada de red a un microservicio de catálogo.
    raise RuntimeError("No hay conexión con el servicio de precios")
