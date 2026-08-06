"""Tests del Módulo 8 - integración.

Empezamos con un test UNITARIO de ejemplo (una pieza aislada).
Tu tarea será escribir un test de INTEGRACIÓN del flujo completo.
"""

import pytest
from pedidos import (
    validar_carrito,
    calcular_subtotal,
    aplicar_impuesto,
    procesar_pedido,
)


# --- Ejemplo: test UNITARIO de una sola pieza ---
def test_calcular_subtotal_unitario():
    carrito = [{"precio": 10}, {"precio": 20}]
    assert calcular_subtotal(carrito) == 30


# --- Tu tarea: test de INTEGRACIÓN del flujo completo ---
def test_procesar_pedido_integracion():
    # Arrange: un carrito con 2 productos (precios 10 y 20 -> subtotal 30)
    carrito = [{"precio": 10}, {"precio": 20}]
    # Act: llama a procesar_pedido(carrito)
    total = procesar_pedido(carrito)
    # Assert: el total con 21% de IVA sobre 30 debe ser 36.3
    assert total == 36.3

# con este test en el que tenemos el carrito vacío comprobamos que el error se propaga por todo el flujo: procesar_pedido[()] llama a validar_carrito([]), que lanza ValueError
def test_procesar_pedido_carrito_vacio():
    carrito = []
    with pytest.raises(ValueError) as excinfo:
        procesar_pedido(carrito)
    assert str(excinfo.value) == "El carrito está vacío"