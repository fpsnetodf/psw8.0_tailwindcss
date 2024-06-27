from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "usuarios/home.html")


def novo(request):
    return render(request, "usuarios/novo.html")


def cadastro(request):
    return render(request, "usuarios/cadastro.html")


def login(request):
    return render(request, "usuarios/login.html")