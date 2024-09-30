from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario
from django.core.serializers import serialize
import json

# Create your views here.
def index(request):
    #Metodo GET
    if request.method == 'GET':
        list_usuarios = Usuario.objects.all()
        usuarios_json = serialize('json', list_usuarios)
        dict_usuarios = json.loads(usuarios_json)
        return JsonResponse(dict_usuarios, safe=False)

    #MEtodo POST
    #Metodo PUT
    #Metodo DELETE
    