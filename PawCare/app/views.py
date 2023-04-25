from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def colab(request):
    return render(request, 'app/colab.html')

def base(request):
    return render(request, 'app/base.html')

def somos(request):
    return render(request, 'app/somos.html')

def servicios(request):
    return render(request, 'app/servicios.html')