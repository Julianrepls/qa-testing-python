"""Tests del Curso 2 - Módulo 2: return_value y side_effect.

TAREA 1 (test_precio_con_iva_ok):
  Usa return_value para que el servicio devuelva un precio base de 100,
  y comprueba que precio_con_iva aplica el 21% -> 121.0

TAREA 2 (test_precio_servicio_caido): la harás en el mini-reto.
"""

from unittest.mock import patch
import tienda
import pytest

@patch("precios_api.obtener_precio_base")
def test_precio_con_iva_ok(mock_precio):

    #   1) haz que el mock devuelva 100  ->  mock_precio.return_value = 100
    mock_precio.return_value = 100

    #   2) llama a tienda.precio_con_iva(...)
    resultado = tienda.precio_con_iva("producto-123")

    #   3) comprueba que el resultado es 121.0
    assert resultado == 121.0
    
@patch("precios_api.obtener_precio_base")
def test_precio_servicio_caido(mock_precio):
    # lo que queremos comprobar es que si el servicio de precios falla, precio_con_iva propaga un RuntimeError. Entonces vamos a 
    # simular un fallo del servicio de precios usando side_effect.

    #   1) haz que el mock lance un RuntimeError ->  mock_precio.side_effect = RuntimeError("No hay conexión con el servicio 
    # de precios")
    
    mock_precio.side_effect = RuntimeError("No hay conexión con el servicio de precios")

    # Ahora lo que va a pasar es que cuando llamemos a tienda.precio_con_iva(...) se va a ejecutar el mock_precio (simulando servidor de precios caido), 
    # que va a lanzar un RuntimeError.
    #   2) llama a tienda.precio_con_iva(...) y comprueba que lanza RuntimeError
    
    with pytest.raises(RuntimeError):
        tienda.precio_con_iva("producto-123")
      
    mock_precio.assert_called_once_with("producto-123")

# Apunte: si queremos comprobar que el mock se llamo pese al fallo, podemos usar: 

# mock_precio.assert_called_once_with("producto-123")