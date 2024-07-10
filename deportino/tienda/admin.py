from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Categoria, Producto, Pedido, Reseña

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'direccion', 'numero_de_telefono']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'direccion', 'numero_de_telefono')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'precio', 'cantidad', 'disponibilidad', 'creado', 'actualizado']
    list_filter = ['disponibilidad', 'creado', 'actualizado']
    list_editable = ['precio', 'cantidad', 'disponibilidad']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha', 'direccion_entrega', 'ciudad_entrega', 'codigo_postal_entrega', 'pagado']
    list_filter = ['pagado', 'fecha']

@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cliente', 'comentario', 'calificacion', 'fecha']
    list_filter = ['calificacion', 'fecha']
    search_fields = ['producto__nombre', 'cliente__nombre']
