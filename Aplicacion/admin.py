from django.contrib import admin
from Aplicacion.models import Hospital, Especialidad, Sector, Estado


# Register your models here.
admin.site.register(Hospital)
admin.site.register(Estado)
admin.site.register(Especialidad)
admin.site.register(Sector)