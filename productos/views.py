from datetime import datetime
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Producto, UsuariosProductos
from .serializers import ProductoSerializer, UsuariosProductosSerializer

"""Listar todos los productos"""
class ProductList(APIView):
    """Clase para consultar todos los productos y crear nuevos"""

    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""Listar producto basado en su ID"""
class ProductDetail(APIView):
    """Clase para consultar, editar o eliminar un producto""" 
    
    #obtener el produto
    def get_prod(self, pk):
        try:
            return Producto.objects.get(id_product=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        #Buscar el producto
        producto = self.get_prod(pk=pk)
        #Lo transformo en diccionario
        serializer = ProductoSerializer(producto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        #Buscar el producto a editar
        producto = self.get_prod(pk=pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Buscar el producto
        producto = self.get_prod(pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""Vista para tabla UsuariosProductos"""
class UsuariosProductosView(APIView):

    """ el =None significa que si no se pasa valor para product_id su valor por defecto sera None. Es decir, el parametro no es obligatorio"""
    def get(self, request, user_id: int = None):
        if user_id:
            usuario_productos=UsuariosProductos.objects.filter(cliente=user_id)
        else:
            usuario_productos=UsuariosProductos.objects.all()
        
        serializer= UsuariosProductosSerializer(usuario_productos, many = True)

        return Response(serializer.data)
    
    def post(self,  request):
        serializer = UsuariosProductosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuarios_productos = UsuariosProductos.objects.create(**serializer.validated_data)
        return Response({"message" : "transaccion exitosa"}, status=status.HTTP_201_CREATED)

class UsuariosProductosDateView(APIView):
    
    def get(self, request):
        
        # GET the value of a GET variable with name 'date_from'
        # Because request.GET is a dictionary, it has the method .get() which retrieves a value for a key in the dictionary
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            # strptime() takes 2 arguments 1. string to be converted to datetime and format code 
            date_from = "2024-10-12"
            date_to = "2024-12-12"
            date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
            date_to = datetime.strptime(date_to,'%Y-%m-%d').date()
            print(date_from, " ", date_to)
            
            # request.user se refiere al usuario con sesion iniciada
            user_product = UsuariosProductos.objects.filter(cliente=request.user.id, fecha_venta__range = [date_from, date_to])
            serializer = UsuariosProductosSerializer(user_product, many = True)
            return Response(serializer.data)

        return Response(data={'message':'no working yet'})

