"""Curso 2 - Módulo 8. Page Object del formulario de login.

Encapsula TODA la interacción con la página de login. Los tests usan esta
clase y NO tocan los selectores directamente. Si cambia un id, se cambia
solo aquí.
"""


class LoginPage:
    def __init__(self, page):
        self.page = page
        # Los selectores viven en UN solo sitio:
        self.usuario = page.locator("#usuario")
        self.password = page.locator("#password")
        self.boton = page.locator("#btn-login")
        self.mensaje = page.locator("#mensaje")

    def cargar(self, url):
        """Abre la página de login."""
        self.page.goto(url)

    def login(self, usuario, password):
        """Rellena el formulario y pulsa Entrar."""
        self.usuario.fill(usuario)
        self.password.fill(password)
        self.boton.click()

    def obtener_mensaje(self):
        """Devuelve el texto del mensaje mostrado."""
        return self.mensaje.inner_text()
