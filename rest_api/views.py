from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Inicio.models import TipoUsuario, Usuario, Region, Comuna, Direccion, Venta, Categoria, TipoProd, Marca, Modelo, Producto, Detalle    
from .serializers import TipoUsuarioSerializer, UsuarioSerializer, RegionSerializer, ComunaSerializer, DireccionSerializer, VentaSerializer, CategoriaSerializer, TipoProdSerializer, MarcaSerializer, ModeloSerializer, ProductoSerializer, DetalleSerializer



# TIPO DE USUARIO
@api_view(['GET', 'POST'])
def listar_tipos_usuario(request):
    if request.method == 'GET':
        tipos_usuario = TipoUsuario.objects.all()
        serializer = TipoUsuarioSerializer(tipos_usuario, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TipoUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_tipo_usuario(request, pk):
    try:
        tipo_usuario = TipoUsuario.objects.get(pk=pk)
    except TipoUsuario.DoesNotExist:
        return Response({'error': 'Tipo de usuario no encontrado'}, status=404)

    if request.method == 'GET':
        serializer = TipoUsuarioSerializer(tipo_usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TipoUsuarioSerializer(tipo_usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tipo_usuario.delete()
        return Response(status=204)


# USUARIO
@api_view(['GET', 'POST'])
def listar_usuarios(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=204)
    
# REGION
@api_view(['GET', 'POST'])
def listar_regiones(request):
    if request.method == 'GET':
        regiones = Region.objects.all()
        serializer = RegionSerializer(regiones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_region(request, pk):
    try:
        region = Region.objects.get(pk=pk)
    except Region.DoesNotExist:
        return Response({'error': 'Region no encontrada'}, status=404)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        region.delete()
        return Response(status=204)


# COMUNA
@api_view(['GET', 'POST'])
def listar_comunas(request):
    if request.method == 'GET':
        comunas = Comuna.objects.all()
        serializer = ComunaSerializer(comunas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ComunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_comuna(request, pk):
    try:
        comuna = Comuna.objects.get(pk=pk)
    except Comuna.DoesNotExist:
        return Response({'error': 'Comuna no encontrada'}, status=404)

    if request.method == 'GET':
        serializer = ComunaSerializer(comuna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ComunaSerializer(comuna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        comuna.delete()
        return Response(status=204)
    

# DIRECCIÓN
@api_view(['GET', 'POST'])
def listar_direcciones(request):
    if request.method == 'GET':
        direcciones = Direccion.objects.all()
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DireccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_direccion(request, pk):
    try:
        direccion = Direccion.objects.get(pk=pk)
    except Direccion.DoesNotExist:
        return Response({'error': 'Direccion no encontrada'}, status=404)

    if request.method == 'GET':
        serializer = DireccionSerializer(direccion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DireccionSerializer(direccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        direccion.delete()
        return Response(status=204)


# VENTA
@api_view(['GET', 'POST'])
def listar_ventas(request):
    if request.method == 'GET':
        ventas = Venta.objects.all()
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_venta(request, pk):
    try:
        venta = Venta.objects.get(pk=pk)
    except Venta.DoesNotExist:
        return Response({'error': 'Venta no encontrada'}, status=404)

    if request.method == 'GET':
        serializer = VentaSerializer(venta)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VentaSerializer(venta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        venta.delete()
        return Response(status=204)
    

# CATEGORÍA
@api_view(['GET', 'POST'])
def listar_categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response({'error': 'Categoria no encontrada'}, status=404)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=204)
    

# TIPO DE PRODUCTO
@api_view(['GET', 'POST'])
def listar_tipos_producto(request):
    if request.method == 'GET':
        tipos_prod = TipoProd.objects.all()
        serializer = TipoProdSerializer(tipos_prod, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TipoProdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_tipo_producto(request, pk):
    try:
        tipo_prod = TipoProd.objects.get(pk=pk)
    except TipoProd.DoesNotExist:
        return Response({'error': 'Tipo de producto no encontrado'}, status=404)

    if request.method == 'GET':
        serializer = TipoProdSerializer(tipo_prod)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TipoProdSerializer(tipo_prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tipo_prod.delete()
        return Response(status=204)


# MARCA
@api_view(['GET', 'POST'])
def listar_marcas(request):
    if request.method == 'GET':
        marcas = Marca.objects.all()
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_marca(request, pk):
    try:
        marca = Marca.objects.get(pk=pk)
    except Marca.DoesNotExist:
        return Response({'error': 'Marca no encontrada'}, status=404)

    if request.method == 'GET':
        serializer = MarcaSerializer(marca)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        marca.delete()
        return Response(status=204)


# MODELO
@api_view(['GET', 'POST'])
def listar_modelos(request):
    if request.method == 'GET':
        modelos = Modelo.objects.all()
        serializer = ModeloSerializer(modelos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ModeloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_modelo(request, pk):
    try:
        modelo = Modelo.objects.get(pk=pk)
    except Modelo.DoesNotExist:
        return Response({'error': 'Modelo no encontrado'}, status=404)

    if request.method == 'GET':
        serializer = ModeloSerializer(modelo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ModeloSerializer(modelo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        modelo.delete()
        return Response(status=204)


# PRODUCTO
@api_view(['GET', 'POST'])
def listar_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=404)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=204)


# DETALLE
@api_view(['GET', 'POST'])
def listar_detalles(request):
    if request.method == 'GET':
        detalles = Detalle.objects.all()
        serializer = DetalleSerializer(detalles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DetalleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_detalle(request, pk):
    try:
        detalle = Detalle.objects.get(pk=pk)
    except Detalle.DoesNotExist:
        return Response({'error': 'Detalle no encontrado'}, status=404)

    if request.method == 'GET':
        serializer = DetalleSerializer(detalle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DetalleSerializer(detalle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        detalle.delete()
        return Response(status=204)
