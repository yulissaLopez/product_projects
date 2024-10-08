from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class Usuario(AbstractUser):
    # se anaden los campos personalizados
    direccion = models.CharField(100, null=True, blank=True, max_length=100)
    pais = models.CharField(max_length=100, default="COLOMBIA")
    date_joined = models.DateTimeField(default=timezone.now)
    

