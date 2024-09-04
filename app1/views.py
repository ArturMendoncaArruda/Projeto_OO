# app1/views.py
from django.shortcuts import render
from rest_framework import generics
from app1.models import Jogo_final
from .serializers import Jogo_finalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import JsonResponse

class UserlistCreate(generics.ListCreateAPIView):
    queryset = Jogo_final.objects.all()
    serializer_class = Jogo_finalSerializer

class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogo_final.objects.all()
    serializer_class = Jogo_finalSerializer




@api_view(['POST'])
def login(request):
    usuario_nome = request.data.get('usuario_nome')
    senha = request.data.get('usuario_senha')

    user = Jogo_final.objects.filter(usuario_nome=usuario_nome).first()
    
    if user:
        # Debug: Verifique os valores
        print(f"Senha armazenada: '{user.usuario_senha}'")
        print(f"Senha fornecida: '{senha}'")
        
        if user.usuario_senha == senha:
            return Response({"message": "Login bem-sucedido"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Senha incorreta"}, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response({"message": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def cadastro(request):
    usuario_nome = request.data.get('usuario_nome')
    if Jogo_final.objects.filter(usuario_nome=usuario_nome).exists():
        return Response({"Usuário já existe, troque de nome"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = Jogo_finalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def token(request):
    return Response({})

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)

def login_page(request):
    return render(request, 'login.html')


def main_page(request):
    return render(request, 'index.html')

def stats_page(request):
    return render(request, 'stats.html')




























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




