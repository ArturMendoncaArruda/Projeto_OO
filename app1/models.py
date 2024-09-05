from django.contrib.auth.models import User
from django.db import models

class Dados_jogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o auth_user
    usuario_nome = models.CharField(max_length=300)
    usuario_senha = models.CharField(max_length=70)
    dinheiro = models.IntegerField(default=0)
    tempo = models.IntegerField(default=0)
    inimigos_derrotados = models.IntegerField(default=0)
