from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = [
        "username",       
        "first_name",     
        "last_name",      
        "email",          
        "password",       
        "is_active",      
        "is_staff",       
        "is_superuser",   
        "last_login",     
        "date_joined"    
    ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('direccion', 'pais')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('direccion', 'pais')}),
    )

admin.site.register(Usuario,UsuarioAdmin)
