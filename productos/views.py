from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from .models import Producto
import json

# Create your views here.
@csrf_exempt
def index(request, pk = None):
    if request.method == "GET":
        if pk:
            # recupera el producto con el id que tiene la pk
            product = Producto.objects.get(id_product=pk)
            products = [product.name_prod, product.price_prod, product.stock_prod]
        else:
            # Values toma las llaves y devuelve los valores a cada llave
            products = list(Producto.objects.all().values("id_product", "name_prod" ,"price_prod", "stock_prod"))

        return JsonResponse(data={"message":"ok", "productos" : products})
    
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

        if pk:
           producto = Producto.objects.get(id_product=pk)
           producto.delete()
        
        # si el id se envia por el cuerpo del request
        # body = request.body.decode('utf-8')
        # request_id = json.loads(body)
        # delete_element = Producto.objects.filter(id_product=request_id['id'])
        # delete_element.delete()

        return JsonResponse(data={'message' : 'ok'})

    if request.method == "PUT":
        if pk:
            # Obtener el producto a editar de la request
            body_unicode = request.body.decode('utf-8')
            # de Json a Python Dict
            body_data = json.loads(body_unicode)

            # busco el inscatce con el id de la request
            product_to_edit = Producto.objects.get(id_product=pk)

            # cambio los valores por los nuevos
            product_to_edit.name_prod = body_data['name_prod']
            product_to_edit.price_prod = body_data['price_prod']
            product_to_edit.stock_prod = body_data['stock_prod']

            #guardo los cambios
            product_to_edit.save()
            product_dict = model_to_dict(product_to_edit)
            return JsonResponse(data={'mensaje' : 'el producto ha sido modificado con exito', 'json' : product_dict})

    if request.method == "PATCH":
        if pk:
        #     # obtengo el id del producto a editar
        #     product_to_edit = Producto.objects.get(id_product=pk)

        #     # obtener la data a cambiar
        #     body_unicode = request.body.decode('utf-8')
        #     data = json.loads(body_unicode)
        #     # Itero sobre el dict_keys y saco el nombre de las claves
        #     for clave, valor in data.items():
        #         #       objeto, nombre_atributo, valor
        #         setattr(product_to_edit, clave, valor)
        
        #     product_to_edit.save()
        #     #print(product_to_edit)
        #     product_dict = model_to_dict(product_to_edit)
        # return JsonResponse(data={'producto' : product_dict})
        
            Producto.objects.filter(id_product=pk).update(name_prod="Huevos De Gallina Feliz")
            return JsonResponse(data={"message" : "product with id = " + str(pk) + " update"})
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
