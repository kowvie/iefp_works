from django.shortcuts import render, redirect, get_object_or_404
from .models import Peca
from .models import Outfit
from .models import Categoria, Estacao
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def lista_pecas(request):
    pecas = Peca.objects.filter(utilizador=request.user)

    categoria_id = request.GET.get('categoria')
    estacao_id = request.GET.get('estacao')

    if categoria_id:
        pecas = pecas.filter(categoria_id=categoria_id)

    if estacao_id:
        pecas = pecas.filter(estacao_id=estacao_id)

    categorias = Categoria.objects.all()
    estacoes = Estacao.objects.all()

    return render(request, 'pecas/pecas_lista.html', {
        'pecas': pecas,
        'categorias': categorias,
        'estacoes': estacoes
    })


@login_required
def criar_peca(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cor = request.POST['cor']
        marca = request.POST['marca']
        tamanho = request.POST['tamanho']
        data = request.POST['data']

        categoria = get_object_or_404(Categoria, id=request.POST['categoria'])
        estacao = get_object_or_404(Estacao, id=request.POST['estacao'])

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

    return render(request, 'pecas/pecas_criar.html', {
        'categorias': categorias,
        'estacoes': estacoes
    })

@login_required
def lista_outfits(request):
    outfits = Outfit.objects.filter(utilizador=request.user)
    return render(request, 'outfit/outfit_lista.html', {'outfits': outfits})

@login_required
def criar_outfit(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        pecas_ids = request.POST.getlist('pecas')

        pecas = Peca.objects.filter(utilizador=request.user, id__in=pecas_ids)
        if pecas.count() != len(pecas_ids):
            return redirect('criar_outfit')

        outfit = Outfit.objects.create(
            nome=nome,
            utilizador=request.user
        )
        outfit.pecas.set(pecas)
        return redirect('lista_outfits')

    pecas = Peca.objects.filter(utilizador=request.user)
    return render(request, 'outfit/outfit_criar.html', {'pecas': pecas})

@login_required
def editar_peca(request, id):
    peca = Peca.objects.get(id=id)

    if request.method == 'POST':
        peca.nome = request.POST['nome']
        peca.cor = request.POST['cor']
        peca.marca = request.POST['marca']
        peca.tamanho = request.POST['tamanho']
        peca.save()
        return redirect('lista_pecas')

    return render(request, 'pecas/pecas_editar.html', {'peca': peca})

@login_required
def apagar_peca(request, id):
    peca = Peca.objects.get(id=id)

    if request.method == 'POST':
        peca.delete()
        return redirect('lista_pecas')

    return render(request, 'pecas/pecas_apagar.html', {'peca': peca})


@login_required
def detalhe_outfit(request, id):
    outfit = Outfit.objects.get(id=id)
    return render(request, 'outfit/outfit_detalhe.html', {'outfit': outfit})

    messages.error(request, "Erro ao criar outfit")
    messages.success(request, "Outfit criado com sucesso")

@login_required
def editar_outfit(request, id):
    outfit = Outfit.objects.get(id=id)

    if request.method == 'POST':
        outfit.nome = request.POST['nome']
        pecas_ids = request.POST.getlist('pecas')

        outfit.save()

        outfit.pecas.set(pecas_ids)

        return redirect('detalhe_outfit', id=outfit.id)

    pecas = Peca.objects.filter(utilizador=request.user)

    return render(request, 'outfit/outfit_editar.html', {
        'outfit': outfit,
        'pecas': pecas
    })