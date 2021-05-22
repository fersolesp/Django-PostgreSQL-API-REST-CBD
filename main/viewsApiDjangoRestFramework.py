from rest_framework import viewsets, permissions, pagination
from .serializers import *
from .models import *
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'size'  # Número de items por página

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all().order_by('id')
    serializer_class = marcaSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class=CustomPageNumberPagination

class CombustibleViewSet(viewsets.ModelViewSet):
    queryset = Combustible.objects.all().order_by('id')
    serializer_class = combustibleSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class=CustomPageNumberPagination

class CajaCambiosViewSet(viewsets.ModelViewSet):
    queryset = CajaCambios.objects.all().order_by('id')
    serializer_class = cajaCambiosSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class=CustomPageNumberPagination

class TraccionViewSet(viewsets.ModelViewSet):
    queryset = Traccion.objects.all().order_by('id')
    serializer_class = traccionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class=CustomPageNumberPagination

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all().order_by('id')
    serializer_class = modeloSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class=CustomPageNumberPagination

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all().order_by('id')
    serializer_class = articuloSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class=CustomPageNumberPagination

class TipoVehiculoViewSet(viewsets.ModelViewSet):
    queryset = TipoVehiculo.objects.all().order_by('id')
    serializer_class = tipoVehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class=CustomPageNumberPagination

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all().order_by('id')
    serializer_class = versionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class=CustomPageNumberPagination
