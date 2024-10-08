from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Solo lectura
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    password = serializers.CharField(write_only=True)  # Solo escritura
    pais = serializers.CharField(max_length=50, required=False)
    direccion = serializers.CharField(max_length=100, required=False)
    date_joined = serializers.DateTimeField(read_only=True)

    def create(self, validate_data):
        # descomprime el diccionario con los datos validados y los pasa como argumentos del modelo.
        user = Usuario(**validate_data)
        #set_password() encripta la contrasena antes de guardarla en la BD
        user.set_password(validate_data['password']) 
        # Guarda el usuario en la BD
        user.save()
        return user