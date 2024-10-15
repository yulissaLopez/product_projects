from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            "id_product",
            "name_prod",
            "price_prod",
            "stock_prod"
        ]
        created_by = serializers.ReadOnlyField(source = 'created_by.username')