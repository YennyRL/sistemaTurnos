from django.test import TestCase
from .models import Usuario, Especialidad
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
        usuario = Usuario.objects.get(dni="Aldo")
        self.assertEqual(usuario.__str__(), "Aldo")

class EspecialidadTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(
            id_especialidad=1,
            nombre_especialidad="ALISADO PELO CORTO"
        )

    def test_especialidad_str(self):
        especialidad = Especialidad.objects.get(nombre_especialidad="ALISADO PELO CORTO")
        self.assertEqual(especialidad.__str__(), "ALISADO PELO CORTO")