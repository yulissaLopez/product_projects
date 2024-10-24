from rest_framework import serializers
from .models import Usuario

#el serializador valida y organiza los datos
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # Campos que se van a serializar
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'direccion',
            'pais',
            'date_joined'
        ]

    # Para serializar todos los campos usar __all__

class InputSerializer(serializers.Serializer):
    # Variables en camelCase por que el front esta en JS
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(min_length = 8)
    firstname = serializers.CharField(source="first_name")
    lastname =  serializers.CharField(source="last_name")
    direccion = serializers.CharField()
    pais = serializers.CharField()

    class Meta:
        abstract = True

class OutputSerializer(InputSerializer):
    password = None
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")

