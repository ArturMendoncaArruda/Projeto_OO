from rest_framework import serializers
from .models import Dados_jogo

class Jogo_finalSerializer(serializers.ModelSerializer):
    class Meta:
        model =Dados_jogo
        fields = ('id', 'user', 'usuario_nome', 'usuario_senha', 'dinheiro', 'tempo', 'inimigos_derrotados')