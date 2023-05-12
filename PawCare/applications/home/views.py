from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView
) 
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

class ColaboradoresView(TemplateView):
    template_name = 'home/colab.html'

class ServicioView(TemplateView):
    template_name = 'home/servicios.html'

class SomosView(TemplateView):
    template_name = 'home/somos.html'

class BaseView(CreateView):
    template_name='base.html'
