from django.contrib import admin
from Aplicacion.models import Hospital, Sector, Estado,Usuario


# Register your models here.
admin.site.register(Hospital)
admin.site.register(Estado)
admin.site.register(Sector)
admin.site.register(Usuario)