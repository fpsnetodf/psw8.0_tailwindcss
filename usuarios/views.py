from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, "usuarios/home.html")


def novo(request):
    return render(request, "usuarios/novo.html")


def cadastro(request):
    
    if request.method == 'GET':
        return render(request, "usuarios/cadastro.html")
    elif request.method == 'POST':
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha') 
        if not senha == confirmar_senha:
            message = "Sua senha não conferi"
            return render(request, "usuarios/cadastro.html", {"message": message})
        if len(senha) < 6:
            message = "a senha dever ter pelo menos 6 digitos"
            return render(request, "usuarios/cadastro.html", {"message": message}) 
        
        user = User.objects.create_user(
            first_name = primeiro_nome, 
            last_name = ultimo_nome, 
            username = username, 
            email = email, 
            password = senha
        )    
        return HttpResponse(f"passou")


def login(request):
    return render(request, "usuarios/login.html")