from django.urls import path
from . import views

urlpatterns = [
    # Listar todos los productos
    path("", views.ProductList.as_view(), name="index"), 
    # Listar detalles de un producto
    path("<int:pk>", views.ProductDetail.as_view(),  name="index"), 
    # Listar usuarios y los productos de ese usuario
    path('usu-prod/<int:user_id>', views.UsuariosProductosView.as_view(), name = 'usuario-productos'),
    path('usu-prod/', views.UsuariosProductosView.as_view(), name='usuario-productos-todos'),
    path('usu-prod-date', views.UsuariosProductosDateView.as_view(), name = 'ususario-productos-fecha' )
]