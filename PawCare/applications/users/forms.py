from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from .models import User, Categoria





class UserRegisterForm(forms.ModelForm):

 


    password1 = forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                 'class': 'formulario__input',
                'placeholder': 'Contraseña',
                'minlength':'4',
                'maxlength':'12'
                
                 
            }
        )
    )


    password2 = forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                 'class': 'formulario__input',
                'placeholder': 'Repetir Contraseña',
                'minlength':'4',
                'maxlength':'12'
            }
        )
    )



    class Meta:

        model = User 
        fields = (
            'username',
            'email',
            'rut',
            'nombres',
            'apellidos',
            'telefono',
            'categoria',
            )
        
        labels={
             'categoria':'Tipo de Usuario',
        }

        widgets = {
             'username': forms.TextInput(
                attrs={
                    'class': 'formulario__input',
                    'placeholder': 'Nombre de usuario...',
                    'minlength':'4',
                    'maxlength':'16'
                }
             ),
             'email': forms.EmailInput(
                attrs={
                     'class': 'formulario__input',
                     'placeholder': 'ejemplo@dominio.com',
                }
             ),
            'rut': forms.TextInput(
                attrs={
                     'class': 'formulario__input',
                     'placeholder': '11222333-4',
                     'minlength':'8',
                     
                }
             ),
            'nombres': forms.TextInput(
                attrs={
                     'class': 'formulario__input',
                     'placeholder': 'Ingresa tus nombre...',
                     'type':'text',
                     'onkeypress':'return SoloLetras(event);',
                }
             ),
            'apellidos': forms.TextInput(
                attrs={
                     'class': 'formulario__input',
                     'placeholder': 'Ingresa tus apellidos...',
                     'onkeypress':'return SoloLetras(event);'
                }
             ),
            'telefono': forms.TextInput(
                attrs={
                     'class': 'formulario__input',
                     'placeholder': '922644388',
                     'minlength':'9',
                }
             ),
             'categoria': forms.Select(
             attrs={
                  'class': 'formulario__input',
                  'id': 'categoria',
             }
             )
        }

    def clean_username(self):
         username= self.cleaned_data['username']
         existe = User.objects.filter(username=username).exists()
         if existe:
              raise ValidationError('El nombre de usuario ya existe')
         return username
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')

class LoginForm(forms.Form):
        username = forms.CharField(
        label='Nombre de usuario',
        required= True,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su usuario',
                'style': '{margin: 10}',
            }
        )
    )
        password = forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña',
            }
        )
    )
        
        def clean(self):
             cleaned_data = super(LoginForm, self).clean()
             username= self.cleaned_data['username']
             password= self.cleaned_data['password']

             if not authenticate(username=username, password=password):
                raise forms.ValidationError('Los datos de usuarios no son correctos')  
             return self.cleaned_data
        
        
            


      
