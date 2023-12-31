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
        return self.nombre

class Especialidad(models.Model):
    id_especialidad=models.AutoField(primary_key=True)
    nombre_especialidad=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_especialidad
    
class Agenda(models.Model):
    #id_profesional=models.AutoField(foreign_key=True)
    dias_laborales=models.DateField(max_length=15) 
    horario_disponible=models.FloatField(max_length=15)
    def __str__(self):
        return  self.horario_disponible 
    
class Profesional(models.Model):
    id_profesional=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    id_servicio=models.AutoField(primary_key=True)
    nombre_servicio=models.CharField(max_length=100)
    duracion_servicio=models.FloatField(max_length=15)
    prof_encargado=models.ForeignKey(Profesional, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombre_servicio 
 
class Turno(models.Model):
    id_turno=models.AutoField(primary_key=True)
    dni_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_profesional=models.ForeignKey(Profesional, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_turno