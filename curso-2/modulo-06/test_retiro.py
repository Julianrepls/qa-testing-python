import pytest
from banco import retirar
# con la conftest.py usa la fixture "cuenta" sin importarla de ningún sitio

def test_retirar_resta_del_saldo(cuenta):
    #cuenta viene de conftest.py con saldo 100
    nuevo_saldo = retirar(cuenta, 40)
    assert nuevo_saldo == 60

# podemos usar mark.smoke para marcar tests críticos / rápidos porque ya hemos registrado el mark en pytest.ini
# de no registrar mark en el pytest.ini, pytest nos daría un warning de "unknown mark". Los tests seguirían funcionando, 
# pero nos avisaría de que no reconoce el mark.
@pytest.mark.smoke
def test_retirar_devuelve_saldo_actualizado(cuenta):
    # Este test lo marcamos como 'smoke' (crítico / rápido)
    assert retirar(cuenta, 40) == 60

def test_retirar_saldo_insuficiente(cuenta):
    #cuenta viene de conftest.py con saldo 100
    with pytest.raises(ValueError) as excinfo:
        retirar(cuenta, 200)
    assert "Saldo insuficiente" in str(excinfo.value)

