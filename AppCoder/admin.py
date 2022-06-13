from django.contrib import admin
from .models import * #importamos

# Register your models here.
# Registramos los modelos

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
#-----------------Clase 24----------------
admin.site.register(Avatar)
