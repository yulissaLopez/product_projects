from rest_framework import serializers
from .models import Usuario

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
 