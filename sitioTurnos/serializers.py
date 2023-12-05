from rest_framework import serializers
from .models import Usuario, Profesional, Especialidad, Servicio, Turno 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'dni', 'nombre', 'apellido', 'email', 'numero_telefono',)

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ('id_profesional', 'nombre','apellido',)

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id_especialidad', 'nombre_especialidad',)

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('id_servicio', 'nombre_servicio', 'duracion_servicio', 'especialidad','profesional_a_cargo',)

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ('id_turno', 'usuario', 'especialidad', 'servicio', 'profesional', 'fecha', 'hora',)