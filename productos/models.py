from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Producto(models.Model):
    id_product = models.IntegerField(primary_key=True)
    name_prod = models.CharField(max_length=50, null=False, blank=False, default="No Aplica")
    price_prod = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock_prod = models.IntegerField(null=False)

    def __str__(self):
        return self.name_prod
    
# Tabla de Usuarios - Productos
class UsuariosProductos(models.Model):
    fecha_venta=models.DateField(verbose_name="Fecha Venta")
    cantidad_producto=models.IntegerField(verbose_name="Cantidad de Productos")
    # Llaves foraneas
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Cliente")
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE,verbose_name="Producto")
        
