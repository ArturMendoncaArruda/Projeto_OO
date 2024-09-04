# app1/urls.py
from django.urls import path, re_path
from .views import UserlistCreate, UserRetrieveUpdateDelete, login_page, main_page, stats_page
from . import views

urlpatterns = [
    path('users', UserlistCreate.as_view(), name='Create-User-List'),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-Details'),
    path('login-page/', login_page, name='login-page'),
    path('main-page/', main_page, name='main-page'),
    path('stats-page/', stats_page, name='stats-page'),
    path('logout/', views.logout_view, name='logout'),
    re_path('login', views.login),
    re_path('cadastro', views.cadastro),
    re_path('token', views.token),
    
    
    
]
