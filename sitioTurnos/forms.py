from django import forms
from .models import Usuario, Especialidad, Servicio, Profesional 


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('dni', 'nombre', 'apellido', 'email', 'numero_telefono')

class TurnoForm(forms.ModelForm):
    class Meta:
        model= Turno
        fields = ('dni_usuario', 'id_profesional', )