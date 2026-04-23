from django.urls import path
from . import views

urlpatterns = [
    path('pecas/', views.lista_pecas, name='lista_pecas'),
    path('pecas/criar/', views.criar_peca, name='criar_peca'),
path('outfits/criar/', views.criar_outfit, name='criar_outfit'),
    path('outfits/', views.lista_outfits, name='lista_outfits'),
]