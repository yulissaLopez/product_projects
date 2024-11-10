from django.contrib import admin
from .models import Producto, UsuariosProductos

# Vincular la tabla del modelo UsuariosProductos al admin de django

class UsuarioProductosAdmin(admin.ModelAdmin):
    model = UsuariosProductos
    list_display = "__all__"
    # Especifica que todos los campos sean clicables
    # Si se hace clic en cualquier campo lo llevara al detalle del registro
    list_display_links = "__all__"

# Register your models here.
admin.site.register(Producto)
admin.site.register(UsuariosProductos)
