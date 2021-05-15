from django.urls import path
from main import views

app_name = 'main'

base_django_api_prefix = 'apiDjangoBase/'

urlpatterns = [
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