from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import Jogo_finalSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Jogo_finalSerializer
