from django.db import models

# Create your models here.
#las clases tienen este formato para luego persistir correctamente 
# #en una bbdd
class Usuario(models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.dni

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
    duracion_servicio=models.DurationField()
    profesional_a_cargo =models.ForeignKey(Profesional, on_delete= models.CASCADE)
    especialidad=models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre_servicio 

class Turno(models.Model):
    id_turno=models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete= models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="fecha de turno")
    hora = models.TimeField(verbose_name="horario de turno")

    def __str__(self):
        return self.id_turno
