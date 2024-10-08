from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from .serializers import UsuarioSerializer
from rest_framework import status
import json

# Create your views here.
@csrf_exempt
def index(request, pk = None):
    #Metodo GET
    if request.method == 'GET':
        if pk:
            # Obtener el usuario especifico / entrega un queryset
            user = Usuario.objects.get(id = pk)
            # Serializo manualmente el queryset y construyo un diccionario
            list_usuarios = {
                'id' : user.id,
                'username' : user.username,
                'email' : user.email,
                'first_name' : user.first_name,
                'last_name' : user.last_name
            }
        else:
            # Obtengo la lista de usuarios creados / me entrega un Queryset
            # # Se obtienen solo los campos necesarios con values
            usuarios = Usuario.objects.all().values('id', 'username', 'email', 'first_name', 'last_name', 'direccion', 'pais', 'date_joined')
            # Covierto el queryset en una lista de diccionarios 
            list_usuarios = list(usuarios)
        return JsonResponse(data={"mensaje" : "200", "Usuarios": list_usuarios})

    #MEtodo POST
    if request.method == 'POST':

        body = request.body.decode('utf-8')
        user_info = json.loads(body)
        serializer = UsuarioSerializer(data=user_info)
        if serializer.is_valid():
            #El metodo save() llama al metdo create() definido en el serializer
            #Se crear la instacia del usuario y se guarda
            user = serializer.save()
            #devuelve los datos del usuario recien creado en formato JSON
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Metodo PUT
    #Metodo DELETE
    