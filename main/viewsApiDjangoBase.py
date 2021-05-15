from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json 
from .models import *
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.postgres.aggregates.general import ArrayAgg

################################################################
## Controladores de los endpoint desarrollados en Django base ##
################################################################

### Marcas ###
@method_decorator(csrf_exempt, name='dispatch')
class MarcaAPI(View):

    def get(self, request, *args, **kwargs):
        MAX_OBJECTS = int(request.headers["Max-Objects"]) if request.headers.get("Max-Objects") else None
        marcas = Marca.objects.all()[:MAX_OBJECTS]
        data = {"results": list(marcas.values("id", "nombre", "url_foto"))}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        marca_json = json.loads(request.body)
        marca = Marca(nombre=marca_json["nombre"], url_foto=marca_json["url_foto"])
        marca.save()
        data = { "status":"created",
            "object": {
                "id": marca.id, 
                "nombre": marca.nombre,
                "url_foto": marca.url_foto,
        }}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def marca_details(request, id):
    marca = get_object_or_404(Marca, id=id)
    data = {}
    if request.method == "GET":
        data = {
            "id": marca.id, 
            "nombre": marca.nombre,
            "url_foto": marca.url_foto,
        }
        return JsonResponse(data)
    elif request.method == "PUT":
        marca_json = json.loads(request.body)
        marca.nombre = marca_json["nombre"]
        marca.url_foto = marca_json["url_foto"]
        marca.save()
        data = { "status":"modified",
            "object": {
                "id": marca.id, 
                "nombre": marca.nombre,
                "url_foto": marca.url_foto,
        }}
    elif request.method == "DELETE":
        marca.delete()
        data = { "status":"deleted"}
    return JsonResponse(data)

### Combustibles ###
@method_decorator(csrf_exempt, name='dispatch')
class CombustibleAPI(View):

    def get(self, request, *args, **kwargs):
        MAX_OBJECTS = int(request.headers["Max-Objects"]) if request.headers.get("Max-Objects") else None
        combustibles = Combustible.objects.all()[:MAX_OBJECTS]
        data = {"results": list(combustibles.values("id", "nombre"))}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        combustible_json = json.loads(request.body)
        combustible = Combustible(nombre=combustible_json["nombre"])
        combustible.save()
        data = { "status":"created",
            "object": {
                "id": combustible.id, 
                "nombre": combustible.nombre,
        }}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def combustible_details(request, id):
    combustible = get_object_or_404(Combustible, id=id)
    data = {}
    if request.method == "GET":
        data = {
            "id": combustible.id, 
            "nombre": combustible.nombre,
        }
        return JsonResponse(data)
    elif request.method == "PUT":
        combustible_json = json.loads(request.body)
        combustible.nombre = combustible_json["nombre"]
        combustible.save()
        data = { "status":"modified",
            "object": {
                "id": combustible.id, 
                "nombre": combustible.nombre,
        }}
    elif request.method == "DELETE":
        combustible.delete()
        data = { "status":"deleted"}
    return JsonResponse(data)

### Cajas de cambio ###
@method_decorator(csrf_exempt, name='dispatch')
class CajaCambiosAPI(View):

    def get(self, request, *args, **kwargs):
        MAX_OBJECTS = int(request.headers["Max-Objects"]) if request.headers.get("Max-Objects") else None
        cajas_cambios = CajaCambios.objects.all()[:MAX_OBJECTS]
        data = {"results": list(cajas_cambios.values("id", "nombre"))}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        caja_cambios_json = json.loads(request.body)
        caja_cambios = CajaCambios(nombre=caja_cambios_json["nombre"])
        caja_cambios.save()
        data = { "status":"created",
            "object": {
                "id": caja_cambios.id, 
                "nombre": caja_cambios.nombre,
        }}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def caja_cambios_details(request, id):
    caja_cambios = get_object_or_404(CajaCambios, id=id)
    data = {}
    if request.method == "GET":
        data = {
            "id": caja_cambios.id, 
            "nombre": caja_cambios.nombre,
        }
        return JsonResponse(data)
    elif request.method == "PUT":
        caja_cambios_json = json.loads(request.body)
        caja_cambios.nombre = caja_cambios_json["nombre"]
        caja_cambios.save()
        data = { "status":"modified",
            "object": {
                "id": caja_cambios.id, 
                "nombre": caja_cambios.nombre,
        }}
    elif request.method == "DELETE":
        caja_cambios.delete()
        data = { "status":"deleted"}
    return JsonResponse(data)

### Tipos de tracción de los vehículos ###
@method_decorator(csrf_exempt, name='dispatch')
class TraccionAPI(View):

    def get(self, request, *args, **kwargs):
        MAX_OBJECTS = int(request.headers["Max-Objects"]) if request.headers.get("Max-Objects") else None
        tracciones = Traccion.objects.all()[:MAX_OBJECTS]
        data = {"results": list(tracciones.values("id", "nombre"))}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        traccion_json = json.loads(request.body)
        traccion = Traccion(nombre=traccion_json["nombre"])
        traccion.save()
        data = { "status":"created",
            "object": {
                "id": traccion.id, 
                "nombre": traccion.nombre,
        }}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def traccion_details(request, id):
    traccion = get_object_or_404(Traccion, id=id)
    data = {}
    if request.method == "GET":
        data = {
            "id": traccion.id, 
            "nombre": traccion.nombre,
        }
        return JsonResponse(data)
    elif request.method == "PUT":
        traccion_json = json.loads(request.body)
        traccion.nombre = traccion_json["nombre"]
        traccion.save()
        data = { "status":"modified",
            "object": {
                "id": traccion.id, 
                "nombre": traccion.nombre,
        }}
    elif request.method == "DELETE":
        traccion.delete()
        data = { "status":"deleted"}
    return JsonResponse(data)

### Modelos ###
@method_decorator(csrf_exempt, name='dispatch')
class ModeloAPI(View):

    def get(self, request, *args, **kwargs):
        MAX_OBJECTS = int(request.headers["Max-Objects"]) if request.headers.get("Max-Objects") else None
        modelos = Modelo.objects.all()[:MAX_OBJECTS]
        data = {"results": list(modelos.values().annotate(combustibles=ArrayAgg('combustibles', distinct=True),cajas_cambios=ArrayAgg('cajas_cambios',distinct=True),tracciones=ArrayAgg('tracciones',distinct=True)))}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        modelo_json = json.loads(request.body)
        modelo = Modelo(nombre=modelo_json["nombre"],marca=get_object_or_404(Marca, id=modelo_json["marca"]),precio=modelo_json["precio"], potencia=modelo_json["potencia"], longitud=modelo_json["longitud"])
        modelo.save()
        modelo.combustibles.add(*modelo_json["combustibles"])
        modelo.cajas_cambios.add(*modelo_json["cajas_cambios"])
        modelo.tracciones.add(*modelo_json["tracciones"])
        modelo.save()
        data = { "status":"created",
            "object": {
                "id": modelo.id, 
                "nombre": modelo.nombre,
                "marca": modelo.marca.id,
                "precio": modelo.precio,
                "longitud": modelo.longitud,
                "potencia": modelo.potencia,
                "combustibles": list(modelo.combustibles.all().values("id")),
                "cajas_cambios": list(modelo.cajas_cambios.all().values("id")),
                "tracciones": list(modelo.tracciones.all().values("id")),
        }}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def modelo_details(request, id):
    modelo = get_object_or_404(Modelo, id=id)
    data = {}
    if request.method == "GET":
        data = {
            "id": modelo.id, 
            "nombre": modelo.nombre,
            "marca": modelo.marca.id,
            "precio": modelo.precio,
            "longitud": modelo.longitud,
            "potencia": modelo.potencia,
            "combustibles": list(modelo.combustibles.all().values("id")),
            "cajas_cambios": list(modelo.cajas_cambios.all().values("id")),
            "tracciones": list(modelo.tracciones.all().values("id")),
        }
        return JsonResponse(data)
    elif request.method == "PUT":
        modelo_json = json.loads(request.body)
        modelo.nombre = modelo_json["nombre"]
        modelo.precio = modelo_json["precio"]
        modelo.longitud = modelo_json["longitud"]
        modelo.marca = None
        modelo.marca = get_object_or_404(Marca, id=modelo_json["marca"])
        modelo.combustibles.clear()
        modelo.combustibles.add(*modelo_json["combustibles"])
        modelo.cajas_cambios.clear()
        modelo.cajas_cambios.add(*modelo_json["cajas_cambios"])
        modelo.tracciones.clear()
        modelo.tracciones.add(*modelo_json["tracciones"])
        modelo.save()
        data = { "status":"modified",
            "object": {
            "id": modelo.id, 
            "nombre": modelo.nombre,
            "marca": modelo.marca.id,
            "precio": modelo.precio,
            "longitud": modelo.longitud,
            "potencia": modelo.potencia,
            "combustibles": list(modelo.combustibles.all().values("id")),
            "cajas_cambios": list(modelo.cajas_cambios.all().values("id")),
            "tracciones": list(modelo.tracciones.all().values("id")),
        }}
    elif request.method == "DELETE":
        modelo.delete()
        data = {"status":"deleted"}
    return JsonResponse(data)

### Artículos ###
@method_decorator(csrf_exempt, name='dispatch')
class ArticuloAPI(View):

    def get(self, request, *args, **kwargs):
        MAX_OBJECTS = int(request.headers["Max-Objects"]) if request.headers.get("Max-Objects") else None
        articulos = Articulo.objects.all()[:MAX_OBJECTS]
        data = {"results": list(articulos.values())}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        articulo_json = json.loads(request.body)
        articulo = Articulo(titulo=articulo_json["titulo"],modelo=get_object_or_404(Modelo, id=articulo_json["modelo"]),url_foto=articulo_json["url_foto"], fecha=articulo_json["fecha"], contenido=articulo_json["contenido"],autor=articulo_json["autor"])
        articulo.save()
        data = { "status":"created",
            "object": {
                "id": articulo.id, 
                "titulo": articulo.titulo,
                "url_foto": articulo.url_foto,
                "fecha": articulo.fecha,
                "contenido": articulo.contenido,
                "autor": articulo.autor,
                "modelo": articulo.modelo.id,
        }}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def articulo_details(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    data = {}
    if request.method == "GET":
        data = {
            "id": articulo.id, 
            "titulo": articulo.titulo,
            "url_foto": articulo.url_foto,
            "fecha": articulo.fecha,
            "contenido": articulo.contenido,
            "autor": articulo.autor,
            "modelo": articulo.modelo.id,
        }
        return JsonResponse(data)
    elif request.method == "PUT":
        articulo_json = json.loads(request.body)
        articulo.titulo = articulo_json["titulo"]
        articulo.url_foto = articulo_json["url_foto"]
        articulo.fecha = articulo_json["fecha"]
        articulo.contenido = articulo_json["contenido"]
        articulo.autor = articulo_json["autor"]
        articulo.modelo = None
        articulo.modelo = get_object_or_404(Modelo, id=articulo_json["modelo"])
        articulo.save()
        data = { "status":"modified",
            "object": {
            "id": articulo.id, 
            "titulo": articulo.titulo,
            "url_foto": articulo.url_foto,
            "fecha": articulo.fecha,
            "contenido": articulo.contenido,
            "autor": articulo.autor,
            "modelo": articulo.modelo.id,
        }}
    elif request.method == "DELETE":
        articulo.delete()
        data = {"status":"deleted"}
    return JsonResponse(data)

### Tipos de vehículo ###
@method_decorator(csrf_exempt, name='dispatch')
class TipoVehiculoAPI(View):

    def get(self, request, *args, **kwargs):
        MAX_OBJECTS = int(request.headers["Max-Objects"]) if request.headers.get("Max-Objects") else None
        tipos_vehiculos = TipoVehiculo.objects.all()[:MAX_OBJECTS]
        data = {"results": list(tipos_vehiculos.values("id", "nombre"))}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        tipo_vehiculo_json = json.loads(request.body)
        tipo_vehiculo = TipoVehiculo(nombre=tipo_vehiculo_json["nombre"])
        tipo_vehiculo.save()
        data = { "status":"created",
            "object": {
                "id": tipo_vehiculo.id, 
                "nombre": tipo_vehiculo.nombre,
        }}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def tipo_vehiculo_details(request, id):
    tipo_vehiculo = get_object_or_404(TipoVehiculo, id=id)
    data = {}
    if request.method == "GET":
        data = {
            "id": tipo_vehiculo.id, 
            "nombre": tipo_vehiculo.nombre,
        }
        return JsonResponse(data)
    elif request.method == "PUT":
        tipo_vehiculo_json = json.loads(request.body)
        tipo_vehiculo.nombre = tipo_vehiculo_json["nombre"]
        tipo_vehiculo.save()
        data = { "status":"modified",
            "object": {
                "id": tipo_vehiculo.id, 
                "nombre": tipo_vehiculo.nombre,
        }}
    elif request.method == "DELETE":
        tipo_vehiculo.delete()
        data = { "status":"deleted"}
    return JsonResponse(data)

### Versiones ###
@method_decorator(csrf_exempt, name='dispatch')
class VersionAPI(View):

    def get(self, request, *args, **kwargs):
        MAX_OBJECTS = int(request.headers["Max-Objects"]) if request.headers.get("Max-Objects") else None
        versiones = Version.objects.all()[:MAX_OBJECTS]
        data = {"results": list(versiones.values())}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        version_json = json.loads(request.body)
        version = Version(nombre=version_json["nombre"],tipo_vehiculo=get_object_or_404(TipoVehiculo, id=version_json["tipo_vehiculo"]),modelo=get_object_or_404(Modelo, id=version_json["modelo"]),url_foto=version_json["url_foto"])
        version.save()
        data = { "status":"created",
            "object": {
                "id": version.id, 
                "nombre": version.nombre,
                "url_foto": version.url_foto,
                "tipo_vehiculo": version.tipo_vehiculo.id,
                "modelo": version.modelo.id
        }}
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def version_details(request, id):
    version = get_object_or_404(Version, id=id)
    data = {}
    if request.method == "GET":
        data = {
            "id": version.id, 
            "nombre": version.nombre,
            "url_foto": version.url_foto,
            "tipo_vehiculo": version.tipo_vehiculo.id,
            "modelo": version.modelo.id
        }
        return JsonResponse(data)
    elif request.method == "PUT":
        version_json = json.loads(request.body)
        version.nombre = version_json["nombre"]
        version.url_foto = version_json["url_foto"]
        version.modelo = None
        version.modelo = get_object_or_404(Modelo, id=version_json["modelo"])
        version.tipo_vehiculo = None
        version.tipo_vehiculo = get_object_or_404(TipoVehiculo, id=version_json["tipo_vehiculo"])
        version.save()
        data = { "status":"modified",
            "object": {
            "id": version.id, 
            "nombre": version.nombre,
            "url_foto": version.url_foto,
            "tipo_vehiculo": version.tipo_vehiculo.id,
            "modelo": version.modelo.id
        }}
    elif request.method == "DELETE":
        version.delete()
        data = {"status":"deleted"}
    return JsonResponse(data)