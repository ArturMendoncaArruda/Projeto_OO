# app1/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')  # Redirecionar para a página inicial após o login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def stats(request):
    return render(request, 'stats.html')

