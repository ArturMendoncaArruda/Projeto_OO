from django.contrib.auth.models import User
from django.db import models

# Classe base abstrata
class BaseJogo(models.Model):
    dinheiro = models.IntegerField(default=0)
    tempo = models.IntegerField(default=0)
    inimigos_derrotados = models.IntegerField(default=0)

    class Meta:
        abstract = True  # Define esta classe como abstrata, sem criar uma tabela no banco de dados

# Classe que herda da base
class Dados_jogo(BaseJogo):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o auth_user
    usuario_nome = models.CharField(max_length=300)
    usuario_senha = models.CharField(max_length=70)
