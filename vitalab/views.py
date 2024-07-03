from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def solicitar_exames(request):
    if request.user.is_authenticated:
        return render(request, 'vitalab/solicitar_exames.html')
    