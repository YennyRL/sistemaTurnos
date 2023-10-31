from django.shortcuts import render
from .forms import UsuarioForm
# Create your views here.
def reservar_turno(request):
    usuario= UsuarioForm()
    return render(request, 'templates/index.html')
