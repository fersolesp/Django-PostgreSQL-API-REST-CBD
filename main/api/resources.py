from rest_framework.permissions import BasePermissionMetaclass
from tastypie.resources import ModelResource
from main.models import *
from tastypie.authentication import *
from tastypie.authorization import *
from tastypie import fields

class MarcaResource(ModelResource):
    class Meta:
        queryset = Marca.objects.all()
        allowed_methods = ['get','post','put','delete']
        authentication = Authentication()
        authorization = Authorization()

class CombustibleResource(ModelResource):
    class Meta:
        queryset = Combustible.objects.all()
        allowed_methods = ['get','post','put','delete']
        authentication = Authentication()
        authorization = Authorization()

class CajaCambiosResource(ModelResource):
    class Meta:
        queryset = CajaCambios.objects.all()
        allowed_methods = ['get','post','put','delete']
        authentication = Authentication()
        authorization = Authorization()

class TraccionResource(ModelResource):
    class Meta:
        queryset = Traccion.objects.all()
        allowed_methods = ['get','post','put','delete']
        authentication = Authentication()
        authorization = Authorization()

class ModeloResource(ModelResource):
    marca = fields.ForeignKey(MarcaResource, full=True, attribute="marca")
    combustibles = fields.ManyToManyField(CombustibleResource, full=True, attribute="combustibles")
    cajas_cambios = fields.ManyToManyField(CajaCambiosResource, full=True, attribute="cajas_cambios")
    tracciones = fields.ManyToManyField(TraccionResource, full=True, attribute="tracciones")

    class Meta:
        queryset = Modelo.objects.all()
        allowed_methods = ['get','post','put','delete']
        authentication = Authentication()
        authorization = Authorization()

class ArticuloResource(ModelResource):
    modelo = fields.ForeignKey(ModeloResource, full=True, attribute="modelo")
    class Meta:
        queryset = Articulo.objects.all()
        allowed_methods = ['get','post','put','delete']
        authentication = Authentication()
        authorization = Authorization()

class TipoVehiculoResource(ModelResource):
    class Meta:
        queryset = TipoVehiculo.objects.all()
        allowed_methods = ['get','post','put','delete']
        authentication = Authentication()
        authorization = Authorization()

class VersionResource(ModelResource):
    modelo = fields.ForeignKey(ModeloResource, full=True, attribute="modelo")
    tipo_vehiculo = fields.ForeignKey(TipoVehiculoResource, full=True, attribute="tipo_vehiculo")

    class Meta:
        queryset = Version.objects.all()
        allowed_methods = ['get','post','put','delete']
        authentication = Authentication()
        authorization = Authorization()