from django.contrib import admin
from main.models import Marca, Modelo, Articulo, Version, TipoVehiculo, Traccion, Combustible, CajaCambios

# Register your models here.
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Articulo)
admin.site.register(Version)
admin.site.register(TipoVehiculo)
admin.site.register(Traccion)
admin.site.register(Combustible)
admin.site.register(CajaCambios)