from django.contrib import admin

from .models import Categoria, Marca, Acessorio

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Acessorio)