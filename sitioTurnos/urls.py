from django.urls import path
from . import views
app_name="turnos"

urlpatterns=[
    path('', views.reservar_turno, name='reservar_turno' )
]