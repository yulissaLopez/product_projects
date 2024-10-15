from .serializers import ProductoSerializer
from .models import Producto
from rest_framework import generics
from rest_framework import permissions

class ProductList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


