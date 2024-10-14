from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class Usuario(AbstractUser):
    # se anaden los campos personalizados
    direccion = models.CharField(max_length=100, null=False, blank=False, default="Galicia")
    pais = models.CharField(max_length=100, default="COLOMBIA")
    

