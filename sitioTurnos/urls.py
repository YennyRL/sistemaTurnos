from django.urls import path
from .views import UsuarioRegistroView
app_name="turnos"

urlpatterns=[
    path('', UsuarioRegistroView.as_view(), name='inicio')
]