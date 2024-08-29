# projeto_final/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URLs do painel de administração
    path('', include('app1.urls')),  # URLs da sua app
]
