from django.contrib import admin

from .models import Autor, Venta, Cliente, Libro, LibroAutor

admin.site.register(Autor)
admin.site.register(Venta)
admin.site.register(Cliente)
admin.site.register(Libro)
admin.site.register(LibroAutor)
