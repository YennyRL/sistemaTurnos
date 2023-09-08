from django.test import TestCase
from .models import Usuario
# Create your tests here.

class UsuarioTestCase(TestCase):
    #setUp sirve para crear la clase a la que le vamos a 
    # realizar el testeo
    def setUp(self):
        Usuario.objects.create(
            dni="12345678",
            nombre="Aldo",
            apellido="Segovia",
            email="aldoo.segovia@gmail.com",
            numero_telefono="1139416887"
        )

    def test_usuario_str(self):
        usuario = Usuario.objects.get(dni="12345678")
        self.assertEqual(usuario.__str__(), "12345678")
