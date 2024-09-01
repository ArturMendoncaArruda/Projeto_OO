# app1/models.py
from django.contrib.auth.models import User
from django.db import models


class Jogo_final(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario_nome = models.CharField(max_length=300)
    usuario_senha = models.CharField(max_length=70)
    dinheiro = models.IntegerField(default=0)
    tempo = models.IntegerField(default=0)
    inimigos_derrotados = models.IntegerField(default=0)
