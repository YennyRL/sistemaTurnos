from django.db import models

# Create your models here.
#las clases tienen este formato para luego persistir correctamente 
# #en una bbdd
class Usuario(models.Model): 
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.dni
