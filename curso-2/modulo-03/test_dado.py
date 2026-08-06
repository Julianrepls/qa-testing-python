from unittest.mock import patch
import dado

@patch("dado.random.randint")
def test_es_seis_verdadero(mock_randint):
    # Simulamos que el dado siempre devuelve 6
    mock_randint.return_value = 6
    assert dado.es_seis() is True

@patch("dado.random.randint")
def test_es_seis_falso(mock_randint):
    # Simulamos que el dado siempre devuelve 1
    mock_randint.return_value = 1
    assert dado.es_seis() is False