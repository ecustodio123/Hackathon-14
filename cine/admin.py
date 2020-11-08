from django.contrib import admin
from .models import Genero, Pelicula, Local, Cartelera

# Register your models here.
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']

admin.site.register(Genero, GeneroAdmin)

class LocalAdmin(admin.ModelAdmin):
    list_display = ['id', 'local', 'status']

admin.site.register(Local, LocalAdmin)

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'user']

admin.site.register(Pelicula, PeliculaAdmin)

class CarteleraAdmin(admin.ModelAdmin):
    list_display = ['id', 'pelicula', 'local', 'horario']

admin.site.register(Cartelera, CarteleraAdmin)