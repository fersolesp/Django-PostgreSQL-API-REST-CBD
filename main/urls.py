from django.conf.urls import url
from django.urls import path, include
from main import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include
from tastypie.api import Api
from main.api.resources import *

app_name = 'main'

# Prefijos de los endpoint de cada API
base_django_api_prefix = 'apiDjangoBase/'
django_rest_framework_api_prefix = 'apiDjangoRestFramework/'
tastypie_api_prefix = 'apiTastypie'

# Registro de la API de Tastypie
v1_api = Api(api_name=tastypie_api_prefix)
v1_api.register(MarcaResource())
v1_api.register(CombustibleResource())
v1_api.register(CajaCambiosResource())
v1_api.register(TraccionResource())
v1_api.register(ModeloResource())
v1_api.register(ArticuloResource())
v1_api.register(TipoVehiculoResource())
v1_api.register(VersionResource())

# Registro de las entidades en el 'router' de Django REST framework
router = routers.DefaultRouter()
api_description = """Endpoints to login and logout:
http://127.0.0.1:8000/apiDjangoRestFramework/rest-auth/login
http://127.0.0.1:8000/apiDjangoRestFramework/rest-auth/logout"""
router.get_api_root_view().cls.__doc__ = api_description
router.register(r'marca', views.MarcaViewSet)
router.register(r'combustible', views.CombustibleViewSet)
router.register(r'cajaCambios', views.CajaCambiosViewSet)
router.register(r'traccion', views.TraccionViewSet)
router.register(r'modelo', views.ModeloViewSet)
router.register(r'articulo', views.ArticuloViewSet)
router.register(r'tipoVehiculo', views.TipoVehiculoViewSet)
router.register(r'version', views.VersionViewSet)

urlpatterns = [
            
    # Endpoints de la API desarrollada con Tastypie
    url('', include(v1_api.urls)),

    # Endpoints de la API desarrollada con Django REST framework
    path(django_rest_framework_api_prefix, include(router.urls)),
    url(django_rest_framework_api_prefix+'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(django_rest_framework_api_prefix+'api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path(django_rest_framework_api_prefix+'rest-auth/', include('rest_auth.urls')),

    # Endpoints de la API desarrollada con Django base
    path(base_django_api_prefix+'marca/', views.MarcaAPI.as_view()),
    path(base_django_api_prefix+'marca/<int:id>/', views.marca_details),
    path(base_django_api_prefix+'combustible/', views.CombustibleAPI.as_view()),
    path(base_django_api_prefix+'combustible/<int:id>/', views.combustible_details),
    path(base_django_api_prefix+'cajaCambios/', views.CajaCambiosAPI.as_view()),
    path(base_django_api_prefix+'cajaCambios/<int:id>/', views.caja_cambios_details),
    path(base_django_api_prefix+'traccion/', views.TraccionAPI.as_view()),
    path(base_django_api_prefix+'traccion/<int:id>/', views.traccion_details),
    path(base_django_api_prefix+'modelo/', views.ModeloAPI.as_view()),
    path(base_django_api_prefix+'modelo/<int:id>/', views.modelo_details),
    path(base_django_api_prefix+'articulo/', views.ArticuloAPI.as_view()),
    path(base_django_api_prefix+'articulo/<int:id>/', views.articulo_details),
    path(base_django_api_prefix+'tipoVehiculo/', views.TipoVehiculoAPI.as_view()),
    path(base_django_api_prefix+'tipoVehiculo/<int:id>/', views.tipo_vehiculo_details),
    path(base_django_api_prefix+'version/', views.VersionAPI.as_view()),
    path(base_django_api_prefix+'version/<int:id>/', views.version_details),
]