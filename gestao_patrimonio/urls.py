from django.contrib import admin
from django.urls import path
from patrimonio import views


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.listar_bens, name='listar_bens'),
    path('bens/criar/', views.criar_bem, name='criar_bem'),
    path('bens/<int:pk>/', views.detalhar_bem, name='detalhar_bem'),
    path('bens/<int:pk>/atualizar/', views.atualizar_bem, name='atualizar_bem'),
    path('bens/<int:pk>/deletar/', views.deletar_bem, name='deletar_bem'),
    path('registrar_movimentacao/', views   .registrar_movimentacao, name='registrar_movimentacao'),
    path('lista_movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('fornecedores/adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('fornecedores/editar/<int:id>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('fornecedores/excluir/<int:id>/', views.excluir_fornecedor, name='excluir_fornecedor'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/adicionar/', views.adicionar_categoria, name='adicionar_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),
]

