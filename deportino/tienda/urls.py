from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CategoriaViewSet, ProductoViewSet, PedidoViewSet, ReseñaViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'reseñas', ReseñaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
