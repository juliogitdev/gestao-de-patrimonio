from django.contrib import admin
from .models import Categoria, Fornecedor, Departamento, Bem, Movimentacao

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Departamento)
admin.site.register(Bem)
admin.site.register(Movimentacao)
