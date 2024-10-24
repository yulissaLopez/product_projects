from rest_framework.decorators import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


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

class SignUp(APIView):
    
    #permisos de la clase
    # Permite que cualquiera pueda acceder  a la clase

    permission_classes =[AllowAny]

    def post(self, request):
        # Validar la data entrante
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if Usuario.objects.filter(email=serialized_data.validated_data['email']).exists():
            return Response("Email already registered", status=status.HTTP_400_BAD_REQUEST)
        
        if Usuario.objects.filter(username=serializer.validated_data['username']).exists():
            return Response("Username already exits", status=status.HTTP_400_BAD_REQUEST)

        # Linea para crear el usuario
        # ** es para desempaquetar datos en python
        user = CustomUser.objects.create_user(**serializer.validated_data)

        #Log in (Getting an access token)
        refresh = RefreshToken.for_user(user)

        serializer = OutputSerializer({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birth_date": user.birth_date,
            "biography": user.biography,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        


    