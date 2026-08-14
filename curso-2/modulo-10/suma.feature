Feature: Calculadora
  Como usuario quiero sumar dos números
  para obtener su total

  Scenario: Sumar dos números positivos
    Given tengo el número 2 y el número 3
    When los sumo
    Then el resultado es 5
  Scenario: Sumar dos números negativos
    Given tengo el número -2 y el número -3
    When los sumo
    Then el resultado es -5