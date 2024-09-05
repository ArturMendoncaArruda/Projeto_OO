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




