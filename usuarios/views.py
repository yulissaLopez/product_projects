from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import generics


# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer