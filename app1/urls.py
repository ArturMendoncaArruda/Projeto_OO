from django.urls import path, re_path
from .views import UserlistCreate, UserRetrieveUpdateDelete, main_page, stats_page
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('users', UserlistCreate.as_view(), name='Create-User-List'),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-Details'),
    path('main-page/', main_page, name='main-page'),
    path('stats-page/', stats_page, name='stats-page'),

    # Login e Logout padrão do Django
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='main-page'), name='logout'),

    # Removi as views de login personalizadas para usar as do Django
    re_path('cadastro', views.cadastro),
    re_path('token', views.token),
]
