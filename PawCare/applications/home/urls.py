from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('home/',views.HomeView.as_view(),name='home',),
    path('colaboradores/',views.ColaboradoresView.as_view(),name='colaboradores',),
    path('servicios/',views.ServicioView.as_view(),name='servicios',),
    path('somos/',views.SomosView.as_view(),name='somos',),

    path('base/', views.BaseView.as_view(),name='base',),


]
