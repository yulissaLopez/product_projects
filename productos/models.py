from django.db import models

# Create your models here.
class Producto(models.Model):
    id_product = models.IntegerField(primary_key=True)
    name_prod = models.CharField(max_length=50, null=False, blank=False, default="No Aplica")
    price_prod = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock_prod = models.IntegerField(null=False)

    def __str__(self):
        return self.name_prod
        
