#Serializador sin DRF

from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta: 
        model = Usuario # modelo 
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'direccion'] #Incluye todos los campos del modelo Usuario