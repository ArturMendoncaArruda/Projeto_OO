# app1/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione campos adicionais aqui
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
