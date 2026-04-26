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

        try:
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
            messages.success(request, "Peça criada com sucesso!")
            return redirect('lista_pecas')
        except:
            messages.error(request, "Erro ao criar peça.")
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
            messages.error(request, "Erro ao criar outfit")
            return redirect('criar_outfit')

        outfit = Outfit.objects.create(
            nome=nome,
            utilizador=request.user
        )
        outfit.pecas.set(pecas)
        messages.success(request, "Outfit criado com sucesso")
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
        messages.success(request, "Peça atualizada com sucesso!")
        return redirect('lista_pecas')

    return render(request, 'pecas/pecas_editar.html', {'peca': peca})

@login_required
def apagar_peca(request, id):
    peca = Peca.objects.get(id=id)

    if request.method == 'POST':
        peca.delete()
        messages.success(request, "Peça apagada com sucesso!")
        return redirect('lista_pecas')

    return render(request, 'pecas/pecas_apagar.html', {'peca': peca})


@login_required
def detalhe_outfit(request, id):
    outfit = Outfit.objects.get(id=id)
    return render(request, 'outfit/outfit_detalhe.html', {'outfit': outfit})

@login_required
def editar_outfit(request, id):
    outfit = Outfit.objects.get(id=id)

    if request.method == 'POST':
        outfit.nome = request.POST['nome']
        pecas_ids = request.POST.getlist('pecas')

        outfit.save()

        outfit.pecas.set(pecas_ids)
        messages.success(request, "Outfit atualizado com sucesso")
        return redirect('detalhe_outfit', id=outfit.id)

    pecas = Peca.objects.filter(utilizador=request.user)

    return render(request, 'outfit/outfit_editar.html', {
        'outfit': outfit,
        'pecas': pecas
    })

@login_required
def usar_peca(request, id):
    peca = get_object_or_404(Peca, id=id, utilizador=request.user)

    peca.frequencia_uso += 1
    peca.save()

    return redirect('lista_pecas')

@login_required
def criar_categoria(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        if nome:
            Categoria.objects.create(nome=nome)
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('lista_categorias')
        else:
            messages.error(request, 'O nome da categoria não pode estar vazio.')
    return render(request, 'categorias/categorias_criar.html')

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categorias_lista.html', {'categorias': categorias})

@login_required
def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST['nome']
        if nome:
            categoria.nome = nome
            categoria.save()
            messages.success(request, 'Categoria editada com sucesso!')
            return redirect('lista_categorias')
        else:
            messages.error(request, 'O nome da categoria não pode estar vazio.')
    return render(request, 'categorias/categorias_editar.html', {'categoria': categoria})

@login_required
def apagar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria apagada com sucesso!')
        return redirect('lista_categorias')
    return render(request, 'categorias/categorias_apagar.html', {'categoria': categoria})

@login_required
def criar_estacao(request):
    if request.method == 'POST':
        nome = request.POST['nome']

        Estacao.objects.create(nome=nome)
        messages.success(request, "Estação criada com sucesso!")
        return redirect('lista_estacoes')

    return render(request, 'estacoes/estacoes_criar.html')

@login_required
def lista_estacoes(request):
    estacoes = Estacao.objects.all()
    return render(request, 'estacoes/estacoes_lista.html', {'estacoes': estacoes})

@login_required
def editar_estacao(request, id):
    estacao = Estacao.objects.get(id=id)

    if request.method == 'POST':
        estacao.nome = request.POST['nome']
        estacao.save()
        messages.success(request, "Estação editada com sucesso")
        return redirect('lista_estacoes')

    return render(request, 'estacoes/estacoes_editar.html', {'estacao': estacao})

@login_required
def apagar_estacao(request, id):
    estacao = Estacao.objects.get(id=id)

    if request.method == 'POST':
        estacao.delete()
        messages.success(request, "Estação apagada com sucesso")
        return redirect('lista_estacoes')

    return render(request, 'estacoes/estacoes_apagar.html', {'estacao': estacao})    