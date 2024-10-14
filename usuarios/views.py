from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def user_list(request, pk):
    """ Listar de usuarios o para crear un usuario """

    if request.method == 'GET':
        users = Usuario.objects.all()
        # Convierte el queryset en un dato nativo de django
        serializer = UsuarioSerializer(users, many=True)
        # serializer.data luego sera transformado en formato JSON por DRF
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """ consultar, actualizar o eliminar un usuario """
    try:
        user = Usuario.objects.get(pk = pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        