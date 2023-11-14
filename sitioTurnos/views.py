
from django.shortcuts import get_list_or_404, render, redirect
from django.views.generic import View
from .forms import UsuarioForm
# Create your views here.

class UsuarioRegistroView(View):
    def get(request, *args, **kwargs):
        context={
        }
        return render(request, 'registro_usuario.html', context)
    
    def post(request, *args, **kwargs):
        context={
        }
        return render(request, 'index.html', context)
