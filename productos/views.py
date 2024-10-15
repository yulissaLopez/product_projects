from .serializers import ProductoSerializer
from .models import Producto
from rest_framework import generics

class ProductList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer 


