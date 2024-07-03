from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TiposExames(models.Model):
    tipo_choices = (
        ('I', 'Exame de imagem'), 
        ('S', 'Exame de sangue')
    )    
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=tipo_choices)
    preco = models.FloatField()
    disponivel = models.BooleanField()
    horario_inicial = models.IntegerField()
    horario_final = models.IntegerField()
    
    def __str__(self):
        return self.nome

class SolicitacaoExame(models.Model):
    choices_status = (
        ('E', 'Em análise'),
        ('F', 'Finalizado')
    )
    usuario = models.ForeignKey(User,  on_delete=models.DO_NOTHING)
    exame = models.ForeignKey(TiposExames,  on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=choices_status)
    resultado = models.FileField(upload_to='resultado', null=True, blank=True)
    requer_senha = models.BooleanField(default=False)
    senha = models.CharField(max_length=6, null=True, blank=True)
    
    def __str__(self):
        return f"{ self.usuario } | { self.exame.nome }"
    
    
class PedidosExames(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exames = models.ManyToManyField(SolicitacaoExame)
    agendado = models.BooleanField(default=True)
    data = models.DateField()

    def __str__(self):
        return f'{self.usuario} | {self.data}'