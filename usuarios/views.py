from rest_framework.decorators import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer


# Create your views here.
class UserList(APIView):
    """Clase para listar todos los usuarios o crear uno nuevo"""
    def get(self, request, format = None):
        user = Usuario.objects.all()
        serializer = UsuarioSerializer(user, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format = None):
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """Clase para consultar, actualizar o eliminar un usuario """
    
    # obtener el usuario
    def get_user(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        user = self.get_user(pk)
        serializer = UsuarioSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
