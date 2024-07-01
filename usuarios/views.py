from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import add_message, constants
from django.contrib.auth import authenticate, login

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
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha') 
        if not senha == confirmar_senha:
            add_message(request, constants.WARNING, "Sua senha não conferi")
            return render(request, "usuarios/cadastro.html")
        if len(senha) < 6:
            add_message(request, constants.ERROR, "a senha dever ter pelo menos 6 digitos")
            return render(request, "usuarios/cadastro.html" ) 
        
        user = User.objects.create_user(
            first_name = primeiro_nome, 
            last_name = ultimo_nome, 
            username = username,              
            password = senha
        ) 
        add_message(request, constants.SUCCESS, "Usuário salvo com sucesso!!")   
        return redirect('cadastro')


def logar(request):
    if request.method == "GET":
        return render(request, "usuarios/login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username = username, password = senha)
        if user:
            login(request, user)
            add_message(request, constants.SUCCESS, f"Seja bem vindo, ao sistema: ")
            return render(request, "usuarios/home.html")
        else: 
            add_message(request, constants.ERROR, 'Username e/ou senha invalidos')
            return render(request, "usuarios/home.html")
        # add_message(request, constants.ERROR, "username ou Senha não conferi")
        # return render(request, 'usuarios/login.html')