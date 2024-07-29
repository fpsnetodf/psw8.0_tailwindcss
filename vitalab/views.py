from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from usuarios.models import PedidosExames, TiposExames
from datetime import datetime

# Create your views here.
# def solicitar_exames(request):
#     if not request.user.is_authenticated:
#         return HttpResponse("Você precisa esta autenticado para acessar a pagina!!")
#     else:   
#         return render(request, 'vitalab/solicitar_exames.html')

@login_required
def solicitar_exames(request): 
    if request.method == "GET": 
        tipos_exames = TiposExames.objects.all()  
        return render(request, 'vitalab/solicitar_exames.html', {"tipos_exames": tipos_exames})  
    
    
def fechar_pedido(request):
    exames_id = request.POST.getlist('exames')

    pedidos_exame = PedidosExames(
        usuario=request.user, 
        data=datetime.now()
        
    )
    pedidos_exame.save()
    return HttpResponse('estou aqui')

      