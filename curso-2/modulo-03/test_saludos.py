"""Tests del Curso 2 - Módulo 3: mockear el tiempo.

Recuerda: se parchea DONDE SE USA -> "saludos.datetime".

TAREA 1 (test_saludo_manana):
  Congela la hora a las 9:00 y comprueba que saludo() == "Buenos días".

TAREA 2 (test_saludo_noche): la harás en el mini-reto.
"""

from datetime import datetime
from unittest.mock import patch
import saludos


@patch("saludos.datetime")
def test_saludo_manana(mock_dt):
    # Congelamos la hora a las 9:00
    mock_dt.now.return_value = datetime(2024, 1, 1, 9, 0, 0)
    assert saludos.saludo() == "Buenos días"
