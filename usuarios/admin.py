from django.contrib import admin
from .models import TiposExames, SolicitacaoExame, PedidosExames
# Register your models here.

admin.site.register(TiposExames)
admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)