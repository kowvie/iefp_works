from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pecas),
    path('pecas/', views.lista_pecas, name='lista_pecas'),
    path('pecas/criar/', views.criar_peca, name='criar_peca'),
    path('outfits/', views.lista_outfits, name='lista_outfits'),
    path('outfits/criar/', views.criar_outfit, name='criar_outfit'),
    path('outfits/<int:id>/', views.detalhe_outfit, name='detalhe_outfit'),
]