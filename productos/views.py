from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from .models import Producto
import json

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "GET":
        # Values toma las llaves y devuelve los valores a cada llave
        products = list(Producto.objects.all().values("id_product", "name_prod" ,"price_prod", "stock_prod"))
        return JsonResponse(data={"message":"ok", "products":products})
    
    #envia informacion del cliente -> servidor
    if request.method == "POST":
        #decodifica el cuerpo de la request en utf / request.body es una cadena de bytes
        body = request.body.decode('utf-8')
        # Lo convierto de json -> diccionario
        request_body = json.loads(body)
        
        producto = Producto.objects.create(
            id_product = request_body['id'],
            name_prod = request_body['name'],
            price_prod = request_body['price'],
            stock_prod = request_body['stock']
        )

        # Convertir en diccionario
        producto_data = {
                'id_product': producto.id_product,
                'name_prod': producto.name_prod,
                'price_prod': str(producto.price_prod),  # Convertir Decimal a string
                'stock_prod': producto.stock_prod
            }


        return JsonResponse(data = {'message' : 'ok', "producto" : producto_data})

    if request.method == "DELETE":
        body = request.body.decode('utf-8')
        request_id = json.loads(body)

        delete_element = Producto.objects.filter(id_product=request_id['id'])
        delete_element.delete()

        return JsonResponse(data={'message' : 'ok'})

# return HttpResponse("Metodo no disponible", status = 405)

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

