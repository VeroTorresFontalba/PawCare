from django.urls import path
from .views import base, home, servicios, somos, colab

urlpatterns = [
    path('', home, name='home'),
    path('base/', base, name='base'),
    path('colaboradores/', colab, name='colaboradores'),
    path('servicios/', servicios, name='servicios'),
    path('somos/', somos, name='somos'),
    
]