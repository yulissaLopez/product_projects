from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductList.as_view(), name="index"),
    path("<int:pk>", views.ProductDetail.as_view(),  name="index"),
]