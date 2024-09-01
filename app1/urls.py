# app1/urls.py
from django.urls import path, re_path
from .views import UserlistCreate, UserRetrieveUpdateDelete
from . import views

urlpatterns = [
    path('users', UserlistCreate.as_view(), name='Create-User-List'),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-Details'),
    re_path('login', views.login),
    re_path('cadastro', views.cadastro),
    re_path('token', views.token),

]
