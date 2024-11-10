from rest_framework import serializers
from .models import Producto , UsuariosProductos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

# Serializador para la tabla UsuariosProductos
class UsuariosProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosProductos
        fields = [
            "fecha_venta",
            "cantidad_producto",
            "cliente",
            "producto"
        ]

# Output serializer
class UsuariosProductOutpuySerializer(serializers.Serializer):
    pass