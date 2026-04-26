from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pecas),
    path('pecas/', views.lista_pecas, name='lista_pecas'),
    path('pecas/criar/', views.criar_peca, name='criar_peca'),
    path('pecas/editar/<int:id>/', views.editar_peca, name='editar_peca'),
    path('pecas/apagar/<int:id>/', views.apagar_peca, name='apagar_peca'),
    path('outfit/', views.lista_outfits, name='lista_outfits'),
    path('outfit/criar/', views.criar_outfit, name='criar_outfit'),
    path('outfit/', views.lista_outfits),
    path('outfit/<int:id>/', views.detalhe_outfit, name='detalhe_outfit'),
    path('outfit/editar/<int:id>/', views.editar_outfit, name='editar_outfit'),
    path('pecas/usar/<int:id>/', views.usar_peca, name='usar_peca'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/apagar/<int:id>/', views.apagar_categoria, name='apagar_categoria'),
    path('estacoes/', views.lista_estacoes, name='lista_estacoes'),
    path('estacoes/criar/', views.criar_estacao, name='criar_estacao'),
    path('estacoes/editar/<int:id>/', views.editar_estacao, name='editar_estacao'),
    path('estacoes/apagar/<int:id>/', views.apagar_estacao, name='apagar_estacao'),
]