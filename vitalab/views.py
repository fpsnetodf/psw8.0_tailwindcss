from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# def solicitar_exames(request):
#     if not request.user.is_authenticated:
#         return HttpResponse("Você precisa esta autenticado para acessar a pagina!!")
#     else:   
#         return render(request, 'vitalab/solicitar_exames.html')

@login_required
def solicitar_exames(request): 
    if request.method == "GET":   
        return render(request, 'vitalab/solicitar_exames.html')  
    
    




      