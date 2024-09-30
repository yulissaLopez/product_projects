from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(AbstractUser):
    direccion = models.CharField(100, null=True, blank=True, max_length=100)
    pais = models.CharField(max_length=100, default="COLOMBIA")
    

