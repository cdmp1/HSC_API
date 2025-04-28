from rest_framework import serializers
from Inicio.models import TipoUsuario, Usuario, Region, Comuna, Direccion, Venta, Categoria, TipoProd, Marca, Modelo, Producto, Detalle 



class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TipoProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProd
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'
