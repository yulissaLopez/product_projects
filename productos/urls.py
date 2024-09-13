from django.urls import path
#from projecto_django.productos import views
from . import views

urlpatterns = [
    path("", views.index, name="index")
]