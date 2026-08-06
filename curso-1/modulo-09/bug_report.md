# 🐛 Bug Report

> Rellena cada sección. Objetivo: que otra persona pueda reproducir el bug
> leyendo SOLO esto, sin preguntarte nada.

**Título:**
DESCUENTO 10% resta cantidad fija en lugar de porcentaje

**Severidad:** Alta
**Prioridad:** Alta

**Entorno:**
Python 3.12, Sistema Operativo Window, cupones.py

**Pasos para reproducir:**
1. Importar aplicar_cupon desde cupones.py
2. Llamar a aplicar_cupon(200, "DESCUENTO10")
3. Comprobar lo que devuelve

**Resultado esperado:**
Aplicar descuento 10%, es decir, esperado 180

**Resultado actual:**
Devuelve mal cada cantidad restanto de manera fija -10, actual 190

**Evidencia / notas:**
Línea 12, return precio - 10
