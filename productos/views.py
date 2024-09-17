from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Producto
import json

# Create your views here.
def index(request):
    if request.method == "GET":
        products = list(Producto.objects.all().values("id_product", "name_prod" ,"price_prod", "stock_prod"))
        return JsonResponse(data={"message":"ok", "products":products})

# anadir productos desde un json
def add(request):
    # abro el json
    with open('productos/productos.json', 'r') as archivo:
        productos = json.load(archivo)

    #Itero sobre los productos y los guardo en una lista de datos
    for producto in productos:
        Producto.objects.create(
            id_product = producto["id"],
            name_prod = producto["nombre"],
            price_prod = producto["precio"],
            stock_prod = producto["stock"]
        )

    
    diccionario = {producto['id'] : producto for producto in productos}
    return JsonResponse(diccionario)

# llenar 5 0 4 productos mas en tabla productos por consola
        