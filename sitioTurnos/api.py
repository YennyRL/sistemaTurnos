from .models import Usuario, Servicio, Profesional, Especialidad, Turno
from .serializers import UsuarioSerializer, ServicioSerializer, ProfesionalSerializer, EspecialidadSerializer, TurnoSerializer
from rest_framework import viewsets, permissions

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EspecialidadSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServicioSerializer

class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesionalSerializer

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TurnoSerializer