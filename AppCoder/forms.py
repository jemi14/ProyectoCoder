from socket import fromshare
from django import forms

#---------------Clase 23-------------------------------
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

#---------------Clase 23-------------------------------
class UserRegisterForm(UserCreationForm):
    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

   #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False) #lo pone para que lo veas pero por ahora no se guarda

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 

        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

#---------------Clase 24-------------------------------
class UserEditForm(UserCreationForm):
    #Acá se define las opciones que queres modificar del usuario,
    #Ponemos las básicas
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    #Especificar los campos
    imagen=forms.ImageField(required=True)

