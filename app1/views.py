# app1/views.py
from django.shortcuts import render
from rest_framework import generics
from app1.models import Dados_jogo
from .serializers import Jogo_finalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

class UserlistCreate(generics.ListCreateAPIView):
    queryset = Dados_jogo.objects.all()
    serializer_class = Jogo_finalSerializer

class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dados_jogo.objects.all()
    serializer_class = Jogo_finalSerializer





    



@api_view(['POST'])
def cadastro(request):
    usuario_nome = request.data.get('usuario_nome')
    usuario_senha = request.data.get('usuario_senha')
    user_id = request.data.get('user')  # ID do usuário para atualizar, se necessário

    # Se o ID do usuário for fornecido, tenta atualizar o usuário existente
    if user_id:
        try:
            user = User.objects.get(id=int(user_id))  # Converte para inteiro
            user.username = usuario_nome
            user.set_password(usuario_senha)  # Atualiza a senha
            user.save()
        except User.DoesNotExist:
            return Response({"user": "Invalid pk - object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Verifica se o nome de usuário já existe
        if User.objects.filter(username=usuario_nome).exists():
            return Response({"Usuário já existe, troque de nome"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Cria um novo usuário
        user = User.objects.create(username=usuario_nome)
        user.set_password(usuario_senha)
        user.save()

    # Cria ou atualiza o registro em Dados_jogo
    jogo_final, created = Dados_jogo.objects.update_or_create(
        user=user,
        defaults={
            'usuario_nome': usuario_nome,
            'usuario_senha': usuario_senha,
        }
    )

    serializer = Jogo_finalSerializer(jogo_final)
    return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

@api_view(['GET'])
def token(request):
    return Response({})


def main_page(request):
    return render(request, 'index.html')

def stats_page(request):
    return render(request, 'stats.html')

#Parte do perfil

@login_required
def profile_page(request):
    return render(request, 'profile.html')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Atualiza o perfil do usuário
        username = request.POST.get('username')
        request.user.username = username
        request.user.save()

        # Atualiza os dados no modelo Dados_jogo
        dados_jogo, created = Dados_jogo.objects.get_or_create(user=request.user)
        dados_jogo.usuario_nome = username
        dados_jogo.save()

        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('profile')
    return render(request, 'username.html')

    
    
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            
            # Atualiza o campo usuario_senha no modelo Dados_jogo
            try:
                dados_jogo = Dados_jogo.objects.get(user=request.user)
                dados_jogo.usuario_senha = form.cleaned_data['new_password1']
                dados_jogo.save()
            except Dados_jogo.DoesNotExist:
                messages.error(request, 'Erro ao encontrar os dados do jogo.')
            
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('profile')
        else:
            print(form.errors)  # Verifique o terminal/log para erros
            messages.error(request, 'Erro ao alterar a senha.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'password.html', {'form': form})

@login_required
def delete_account(request):
    user = request.user
    user.delete()
    logout(request)  
    return redirect('main-page')   




def update_jogo_final(request, id):
    try:
        jogo_final = Dados_jogo.objects.get(id=id)
    except Dados_jogo.DoesNotExist:
        return Response({"message": "Registro não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = Jogo_finalSerializer(jogo_final, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})


























#csrf_exempt
#def jogo_finalApi(request, id=0):
    #if request.method=='GET':
     #   usuario = Jogo_final.objects.all()
      #  usuario_serializer=Jogo_finalSerializer(usuario,many=True)
       # return JsonResponse(usuario_serializer.data,safe=False)
#    elif request.method=='POST':
 #       usuario_data=JSONParser.parse(request)
  #      usuario_serializer=Jogo_finalSerializer(data=usuario_data)
   #     if usuario_serializer.is_valid():
    #        usuario_serializer.save()
     #       return JsonResponse("Adicionado com sucesso",safe=False)
      #  return JsonResponse("Não foi possível adicionar",safe=False)
#    elif request.method=='PUT':
 #       usuario_data=JSONParser.parse(request)
  #      user=Jogo_final.objects.get(id_usuario=usuario_data['id_usuario'])
   #     usuario_serializer=Jogo_finalSerializer(user,data=usuario_data)
    #    if usuario_serializer.is_valid():
     #       usuario_serializer.save()
      #      return JsonResponse("Adicionado com sucesso",safe=False)
       # return JsonResponse("Não foi adicionado")
#    elif request.method=='DELETE':
 #       user=Jogo_final.objects.get(id_usuario=usuario_data['id_usuario'])
  #      user.delete()
   #     return JsonResponse("Deletado com sucesso",safe=False)




