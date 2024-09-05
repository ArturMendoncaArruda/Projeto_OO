from rest_framework import viewsets
from django.contrib import admin
from django.contrib.auth.models import User
from .serializers import Jogo_finalSerializer
from .models import Dados_jogo

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Jogo_finalSerializer


admin.site.register(Dados_jogo)