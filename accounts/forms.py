from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class CustomUserChangeForm(UserChangeForm):
    # Ocultamos el campo de contraseña para que no se muestre en el formulario de edición del perfil.
    password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

