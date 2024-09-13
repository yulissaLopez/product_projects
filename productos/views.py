from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Producto

# Create your views here.
def index(request):
    if request.method == "GET":
        products = list(Producto.objects.all().values("id_product", "name_prod" ,"price_prod", "stock_prod"))
        return JsonResponse(data={"message":"ok", "products":products})

# llenar 5 0 4 productos mas en tabla productos por consola
        