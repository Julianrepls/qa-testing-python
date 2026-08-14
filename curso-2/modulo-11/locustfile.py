"""Curso 2 - Módulo 11. Prueba de carga con Locust.

Define un 'usuario virtual' que golpea el servidor. Locust lanzará muchos
de estos a la vez y medirá RPS, tiempos de respuesta y percentiles.

Se ejecuta (contra un servidor local en el puerto 8000), en modo headless:

  locust -f locustfile.py --headless -u 10 -r 2 --run-time 10s --host http://localhost:8000

  -u 10        -> 10 usuarios concurrentes
  -r 2         -> aparecen a 2 por segundo (spawn rate)
  --run-time   -> dura 10 segundos
  --host       -> a qué servidor atacar
"""

from locust import HttpUser, task, between


class UsuarioWeb(HttpUser):
    # Cada usuario espera entre 1 y 2 segundos entre acciones
    wait_time = between(1, 2)

    @task
    def ver_home(self):
        self.client.get("/")
