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
    path('outfits/', views.lista_outfits),
    path('outfit/<int:id>/', views.detalhe_outfit, name='detalhe_outfit'),
]