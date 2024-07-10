from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Crea tus modelos aquí.

class Usuario(AbstractUser):
    direccion = models.CharField(max_length=255)
    numero_de_telefono = models.CharField(max_length=10)
    grupos = models.ManyToManyField(
        Group,
        related_name='usuarios_con_grupos',  # Cambiamos el related_name
        blank=True,
        help_text=('Los grupos a los que pertenece este usuario. Un usuario obtendrá todos los permisos '
                   'otorgados a cada uno de sus grupos.'),
        verbose_name=('grupos'),
    )
    permisos_de_usuario = models.ManyToManyField(
        Permission,
        related_name='usuarios_con_permisos',  # Cambiamos el related_name
        blank=True,
        help_text=('Permisos específicos para este usuario.'),
        verbose_name=('permisos de usuario'),
    )
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['nombre']
        indexes = [models.Index(fields=['nombre']),]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d', blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=False)
    cantidad = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['nombre']),
            models.Index(fields=['creado']),
        ]

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Usuario, related_name='pedidos', on_delete=models.CASCADE)
    fecha = models.DateField()
    direccion_entrega = models.CharField(max_length=250)
    ciudad_entrega = models.CharField(max_length=100)
    codigo_postal_entrega = models.CharField(max_length=10)
    pagado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f'Pedido {self.id}'

class Reseña(models.Model):
    producto = models.ForeignKey(Producto, related_name='reseñas', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, related_name='reseñas', on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'reseña'
        verbose_name_plural = 'reseñas'
        ordering = ['-fecha']

    def __str__(self):
        return f'Reseña de {self.cliente} para {self.producto}'     