from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin 

from .managers import UserManager

from applications.categoria.models import Categoria

# Create your models here.
class User (AbstractBaseUser, PermissionsMixin, models.Model ):

    TIPOUSER_CHOICES = (
        ('CL','Cliente'),
        ('CU','Cuidador')
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    rut = models.CharField(max_length=10)
    nombres= models.CharField(max_length=100, blank=True)
    apellidos= models.CharField(max_length=100 ,blank=True)
    telefono= models.CharField(max_length=9,blank=True)
    tipodeusuario=models.CharField(max_length=2,choices=TIPOUSER_CHOICES)
    #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #
    is_staff = models.BooleanField(default=False) #para especificar si el usuario es administrador

    USERNAME_FIELD ='username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username
    def get_full_name(self):
        return self.nombres+" "+self.apellidos