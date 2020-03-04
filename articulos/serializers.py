from rest_framework import serializers
from .models import Articulo, Contenido
from revista.models import *
from revista.serializers import *
from patrocinadores.models import Patrocinador


#serializador para sacar nombre de los articulos
class NomArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model       =   Articulo
        fields      =   ['titulo']

#serializador para sacar para serializador de articulos
# class DatosContenidoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model       =   Contenido
#         fields      =   ['tipo','recurso','alt']


#serializador para CRUD del modelo contenido
class POSTContenidoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    articulo    =   serializers.PrimaryKeyRelatedField(
                        queryset=Articulo.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model   =   Contenido
        fields  =   '__all__'

#serializador para sacar datos de contenidos
class ContenidoSerializer(serializers.ModelSerializer):
    #articulo  =   NomArticuloSerializer(read_only=True)
    class Meta:
        model       =   Contenido
        exclude      =  ['articulo']


#serializador para sacar nombre de la revista
class NomRevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista']


#serializador para sacar nombre de categoria
class NomCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Categorias
        fields  =   ['id','nombre_categoria', 'icono']

#serializador para sacar nombre de subcategoria
class NomSubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Subcategorias
        fields  =   ['id','nombre_subcategoria']


#serializador para sacar datos de los articulos
class ArticuloSerializer(serializers.ModelSerializer):
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['id', 'titulo', 'imagen','redactado_por','fecha_publicacion','categoria', 'subcategoria', 'slug']



#Detalle Articulo
class DetalleArticuloSerializer(serializers.ModelSerializer):
    #origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    con_art         =   ContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['id', 'titulo', 'imagen', 'con_art','redactado_por','fecha_publicacion','categoria', 'subcategoria', 'slug']



#serializador para CRUD de articulos
class POSTArticuloSerializer(serializers.ModelSerializer):
    
    origen_revista  =   serializers.PrimaryKeyRelatedField(
                        queryset=Revista.objects.all(),
                        required=True,
                        many=False)
    categoria       =   serializers.PrimaryKeyRelatedField(
                        queryset=Categorias.objects.all(),
                        required=True,
                        many=False)
    subcategoria    =   serializers.PrimaryKeyRelatedField(
                        queryset=Subcategorias.objects.all(),
                        required=True,
                        many=False)
    con_art         =   POSTContenidoSerializer(many=True)

    class Meta:
        model       =   Articulo
        fields      =   '__all__'

    def create(self,validated_data):
        print(validated_data)
        contenido_articulo=validated_data.pop('con_art')
        articulo=Articulo.objects.create(**validated_data)
        for o in contenido_articulo:
            tipo    =o['tipo']  
            recurso =o['recurso']
            alt     =o['alt']
            Contenido.objects.create(articulo=articulo, tipo=tipo, recurso=recurso,  alt=alt)
        return articulo
        
    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.subcategoria = validated_data.get('subcategoria', instance.subcategoria)
        instance.en_portada = validated_data.get('en_portada', instance.en_portada)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.redactado_por = validated_data.get('redactado_por', instance.redactado_por)
        instance.publicado = validated_data.get('publicado', instance.publicado)
        instance.cortesia_de = validated_data.get('cortesia_de', instance.cortesia_de)
        instance.fecha_publicacion = validated_data.get('fecha_publicacion', instance.fecha_publicacion)
        instance.fecha_fin = validated_data.get('fecha_fin', instance.fecha_fin)
        instance.fecha_creacion = validated_data.get('fecha_creacion', instance.fecha_creacion)
        instance.fecha_modificacion = validated_data.get('fecha_modificacion', instance.fecha_modificacion)

        #instance.title = validated_data.get('title', instance.title)
        instance.save()



        items = validated_data.get('con_art')
        for item in items:
            item_id = item.get('id', None)
            print(item)
            if item_id:
                inv_item = Contenido.objects.get(id=item_id, articulo=instance)
                inv_item.tipo = item.get('tipo', inv_item.tipo)
                inv_item.recurso = item.get('recurso', inv_item.recurso)
                inv_item.alt = item.get('alt', inv_item.alt)
                inv_item.save()
            else:
                print("no se modifico el contenido")
        return instance


#serializador para sacar datos de articulos especiales
class EspecialArticuloSerializer(serializers.ModelSerializer):
    #origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    #con_art         =   DatosContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['id','titulo','imagen','en_portada','categoria','subcategoria', 'redactado_por','cortesia_de','fecha_publicacion','slug']
    

