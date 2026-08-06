"""Tests del Curso 2 - Módulo 1: Mocking.

OBJETIVO: probar registrar_usuario SIN enviar un email de verdad.
Usaremos @patch para sustituir notificador.enviar_bienvenida por un mock.

Tu tarea (test_registrar_usuario_ok):
  1) El decorador @patch ya está puesto: inyecta 'mock_enviar' como parámetro.
  2) Llama a registrar_usuario("ana@mail.com").
  3) Comprueba que:
       - devuelve {"email": "ana@mail.com", "activo": True}
       - el email de bienvenida se intentó enviar UNA vez con "ana@mail.com"
         (pista: mock_enviar.assert_called_once_with(...))
"""

from unittest.mock import patch
import usuarios
import pytest

@patch("notificador.enviar_bienvenida")
def test_registrar_usuario_ok(mock_enviar):
    
    # Tenemos que llamar a registrar_usuario y tenemos dos opciones: o (import usuarios) y llamarlo usuarios.registrar_usuario, 
    # o (from usuarios import registrar_usuario) y llamarlo registrar_usuario. En este caso, hemos optado por la primera opción.  
    resultado = usuarios.registrar_usuario("ana@mail.com")

    assert resultado == {"email": "ana@mail.com", "activo": True}
    mock_enviar.assert_called_once_with("ana@mail.com")

@patch("notificador.enviar_bienvenida")
def test_registrar_usuario_email_invalido(mock_enviar):
    with pytest.raises(ValueError):
        usuarios.registrar_usuario("ana.mail.com")
    
    # Comprobamos que no se ha llamado a enviar_bienvenida
    mock_enviar.assert_not_called()