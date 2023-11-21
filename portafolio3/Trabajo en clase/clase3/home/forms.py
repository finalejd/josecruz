from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#Formulario de login
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu nombre"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu contraseña"}))

#Formulario de creacion de usuario
class UserForm(UserCreationForm):

    username=forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Enter your username"}))
    password1=forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Enter your password"}))
    password2=forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Repeat your password"}))
    first_name =forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Enter your firts name"}))
    last_name=forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Enter your last name"}))
    email =forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Enter your email"}))

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email"
        ]


