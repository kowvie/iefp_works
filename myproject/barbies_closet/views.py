from django.shortcuts import render, redirect
from .models import Peca
from .models import Outfit
from .models import Categoria, Estacao

def lista_pecas(request):
    pecas = Peca.objects.filter(utilizador=request.user)
    return render(request, 'pecas/lista.html', {'pecas': pecas})

def criar_peca(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cor = request.POST['cor']
        marca = request.POST['marca']
        tamanho = request.POST['tamanho']
        data = request.POST['data']
        categoria = Categoria.objects.get(id=request.POST['categoria'])
        estacao = Estacao.objects.get(id=request.POST['estacao'])

        Peca.objects.create(
            utilizador=request.user,
            nome=nome,
            cor=cor,
            marca=marca,
            tamanho=tamanho,
            data_aquisicao=data,
            categoria=categoria,
            estacao=estacao
        )
        return redirect('lista_pecas')

    categorias = Categoria.objects.all()
    estacoes = Estacao.objects.all()

    return render(request, 'pecas/criar.html', {
        'categorias': categorias,
        'estacoes': estacoes
    })

def lista_outfits(request):
    outfits = Outfit.objects.filter(utilizador=request.user)
    return render(request, 'outfits/lista.html', {'outfits': outfits})

def criar_outfit(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        pecas_ids = request.POST.getlist('pecas')

        outfit = Outfit.objects.create(
            nome=nome,
            utilizador=request.user
        )

        outfit.pecas.set(pecas_ids)

        return redirect('lista_outfits')

    pecas = Peca.objects.filter(utilizador=request.user)
    return render(request, 'outfits/criar.html', {'pecas': pecas})