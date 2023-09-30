from django.contrib import admin
from .models import Persona,Producto, Orden, Mascota, Libro, Pelicula, Articulo, Comentario, Calificacion, Imagen
# Register your models here.
#se importan al adminsite los modelos(tablas)
admin.site.register(Persona)#.....1
admin.site.register(Producto)#....2
admin.site.register(Orden)#.......3
admin.site.register(Mascota)#.....4
admin.site.register(Libro)#.......5
admin.site.register(Pelicula)#....6
admin.site.register(Articulo)#....7
admin.site.register(Comentario)#..8
admin.site.register(Calificacion)#9
admin.site.register(Imagen)#.....10
