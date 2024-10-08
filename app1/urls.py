from django.urls import path, re_path
from .views import UserlistCreate, UserRetrieveUpdateDelete, main_page, stats_page, profile_page, edit_profile, change_password, delete_account, sign_in, feedback_page, login_para_godot, aumentar_dinheiro, get_dinheiro
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import csrf_token_view

urlpatterns = [
    path('users', UserlistCreate.as_view(), name='Create-User-List'),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-Details'),
    path('main-page/', main_page, name='main-page'),
    path('stats-page/', stats_page, name='stats-page'),
    path('get-csrf-token/', csrf_token_view, name='csrf-token'),
    path('sign-in/', sign_in, name='sign-in'),
    path('profile/', profile_page, name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('change-password/', change_password, name='change-password'),
    path('delete-account/', delete_account, name='delete-account'),
    path('feedback-page/', feedback_page, name='feedback-page'),
    path('godot/', login_para_godot, name='godot'),
    path('dinheiro', aumentar_dinheiro, name='dinheiro'),
    path('get_dinheiro', get_dinheiro, name='pegar_dinheiro'),
    # Login e Logout padrão do Django
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='main-page'), name='logout'),
    #///
   
    re_path('cadastro', views.cadastro),
    re_path('token', views.token),
]
