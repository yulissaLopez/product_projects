from django.urls import path
#from projecto_django.productos import views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.index, name="index"),
    path('add', views.add, name = "add")
]