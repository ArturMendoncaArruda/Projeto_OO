from rest_framework import serializers
from .models import Jogo_final

class Jogo_finalSerializer(serializers.ModelSerializer):
    class Meta:
        model =Jogo_final
        fields = ('id_usuario', 'usuario_nome', 'usuario_senha', 'dinheiro', 'tempo', 'inimigos_derrotados')