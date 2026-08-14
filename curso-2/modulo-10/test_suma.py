"""Curso 2 - Módulo 10: BDD con pytest-bdd.

Este archivo conecta el escenario de 'suma.feature' con código Python.
Cada frase Given/When/Then se implementa con una función decorada.

Usamos un dict 'contexto' para pasar datos entre pasos (los números y el
resultado), porque cada step es una función independiente.
"""

from pytest_bdd import scenarios, given, when, then
from calculadora import sumar

# Carga TODOS los escenarios del archivo .feature
scenarios("suma.feature")


@given("tengo el número 2 y el número 3", target_fixture="contexto")
def contexto():
    return {"a": 2, "b": 3}


@when("los sumo")
def sumar_numeros(contexto):
    contexto["resultado"] = sumar(contexto["a"], contexto["b"])


@then("el resultado es 5")
def comprobar_resultado(contexto):
    assert contexto["resultado"] == 5


@given("tengo el número -2 y el número -3", target_fixture="contexto")
def contexto_negativos():
    return {"a": -2, "b": -3}

@when("los sumo")
def sumar_negativos(contexto):
    contexto["resultado"] = sumar(contexto["a"], contexto["b"])

@then("el resultado es -5")
def comprobar_negativos(contexto):
    assert contexto["resultado"] == -5