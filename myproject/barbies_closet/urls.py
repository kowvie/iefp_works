from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pecas, name='lista_pecas'),
    path('create/', views.criar_peca, name='criar_peca'),
]