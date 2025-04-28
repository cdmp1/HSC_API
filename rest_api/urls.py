from django.urls import path
from . import views



urlpatterns = [

    # TIPOS DE USUARIO
    path('tipos_usuario/', views.listar_tipos_usuario, name='listar_tipos_usuario'),
    path('tipos_usuario/<int:pk>/', views.detalle_tipo_usuario, name='detalle_tipo_usuario'),

    # USUARIO
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/<str:pk>/', views.detalle_usuario, name='detalle_usuario'), 

    # REGIONES
    path('regiones/', views.listar_regiones, name='listar_regiones'),
    path('regiones/<int:pk>/', views.detalle_region, name='detalle_region'),

    # COMUNAS
    path('comunas/', views.listar_comunas, name='listar_comunas'),
    path('comunas/<int:pk>/', views.detalle_comuna, name='detalle_comuna'),

    # DIRECCIONES
    path('direcciones/', views.listar_direcciones, name='listar_direcciones'),
    path('direcciones/<int:pk>/', views.detalle_direccion, name='detalle_direccion'),

    # VENTAS
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/<int:pk>/', views.detalle_venta, name='detalle_venta'),

    # CATEGORÍAS
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/<int:pk>/', views.detalle_categoria, name='detalle_categoria'),

    # TIPOS DE PRODUCTO
    path('tipos_producto/', views.listar_tipos_producto, name='listar_tipos_producto'),
    path('tipos_producto/<int:pk>/', views.detalle_tipo_producto, name='detalle_tipo_producto'),

    # MARCAS
    path('marcas/', views.listar_marcas, name='listar_marcas'),
    path('marcas/<int:pk>/', views.detalle_marca, name='detalle_marca'),

    # MODELOS
    path('modelos/', views.listar_modelos, name='listar_modelos'),
    path('modelos/<int:pk>/', views.detalle_modelo, name='detalle_modelo'),

    # PRODUCTOS
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),

    # DETALLES
    path('detalles/', views.listar_detalles, name='listar_detalles'),
    path('detalles/<int:pk>/', views.detalle_detalle, name='detalle_detalle'),

]
