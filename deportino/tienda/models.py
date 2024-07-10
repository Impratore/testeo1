from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    direccion = models.CharField(
        max_length=255, 
        help_text='Dirección del usuario.'
    )
    numero_de_telefono = models.CharField(
        max_length=10, 
        help_text='Número de teléfono del usuario.'
    )
    grupos = models.ManyToManyField(
        Group,
        related_name='usuarios_con_grupos',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.',
        verbose_name='grupos',
    )
    permisos_de_usuario = models.ManyToManyField(
        Permission,
        related_name='usuarios_con_permisos',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos de usuario',
    )

class Categoria(models.Model):
    nombre = models.CharField(
        max_length=200, 
        help_text='Nombre de la categoría.'
    )
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        help_text='Slug único para la categoría.'
    )

    class Meta:
        ordering = ['nombre']
        indexes = [models.Index(fields=['nombre']),]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model): 
    categoria = models.ForeignKey(
        Categoria, 
        related_name='productos', 
        on_delete=models.CASCADE,
        help_text='Categoría a la que pertenece el producto.'
    )
    nombre = models.CharField(
        max_length=200, 
        help_text='Nombre del producto.'
    )
    slug = models.SlugField(
        max_length=200, 
        help_text='Slug del producto.'
    )
    imagen = models.ImageField(
        upload_to='productos/%Y/%m/%d', 
        blank=True,
        help_text='Imagen del producto.'
    )
    descripcion = models.TextField(
        blank=True,
        help_text='Descripción del producto.'
    )
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text='Precio del producto.'
    )
    disponibilidad = models.BooleanField(
        default=False,
        help_text='Indica si el producto está disponible.'
    )
    cantidad = models.IntegerField(
        default=0,
        help_text='Cantidad de productos en stock.'
    )
    creado = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha de creación del producto.'
    )
    actualizado = models.DateTimeField(
        auto_now=True,
        help_text='Fecha de última actualización del producto.'
    )

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
    cliente = models.ForeignKey(
        Usuario, 
        related_name='pedidos', 
        on_delete=models.CASCADE,
        help_text='Cliente que realizó el pedido.'
    )
    fecha_pedido = models.DateTimeField(
        auto_now_add=True, 
        help_text='Fecha y hora en que se realizó el pedido.'
    )
    fecha_entrega_deseada = models.DateField(
        help_text='Fecha deseada para la entrega del pedido.'
    )
    direccion_entrega = models.CharField(
        max_length=250, 
        help_text='Dirección de entrega del pedido.'
    )
    ciudad_entrega = models.CharField(
        max_length=100, 
        help_text='Ciudad de entrega del pedido.'
    )
    codigo_postal_entrega = models.CharField(
        max_length=10, 
        help_text='Código postal de la dirección de entrega.'
    )
    pagado = models.BooleanField(
        default=False, 
        help_text='Indica si el pedido ha sido pagado.'
    )

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f'Pedido {self.id}'

class Reseña(models.Model):
    producto = models.ForeignKey(
        Producto, 
        related_name='reseñas', 
        on_delete=models.CASCADE,
        help_text='Producto al que se refiere la reseña.'
    )
    cliente = models.ForeignKey(
        Usuario, 
        related_name='reseñas', 
        on_delete=models.CASCADE,
        help_text='Cliente que escribió la reseña.'
    )
    comentario = models.TextField(
        help_text='Comentario del cliente sobre el producto.'
    )
    calificacion = models.PositiveIntegerField(
        help_text='Calificación del producto (1-5).'
    )
    fecha = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha en que se escribió la reseña.'
    )

    class Meta:
        verbose_name = 'reseña'
        verbose_name_plural = 'reseñas'
        ordering = ['-fecha']

    def __str__(self):
        return f'Reseña de {self.cliente} para {self.producto}'
    