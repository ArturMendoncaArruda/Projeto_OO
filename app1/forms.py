# app1/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de Usuário', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
