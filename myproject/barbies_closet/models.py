from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Estacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Peca(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=10)
    data_aquisicao = models.DateField()
    frequencia_uso = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    estacao = models.ForeignKey(Estacao, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


class Outfit(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)

    pecas = models.ManyToManyField(Peca)

    def __str__(self):
        return self.nome
