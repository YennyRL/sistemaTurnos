from rest_framework import routers
from .api import UsuarioViewSet, ServicioViewSet, ProfesionalViewSet, EspecialidadViewSet, TurnoViewSet
router = routers.DefaultRouter()

router.register(r'api/Usuarios', UsuarioViewSet, basename='usuarios' )
router.register(r'api/Servicios', ServicioViewSet, basename='servicios')
router.register(r'api/Profesionales', ProfesionalViewSet, basename='profesionales')
router.register(r'api/Especialidades', EspecialidadViewSet, basename='especialidades')
router.register(r'api/Turnos', TurnoViewSet, basename='Turnos')

urlpatterns = router.urls