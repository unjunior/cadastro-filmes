from django.shortcuts import render, redirect,get_object_or_404
from .models import Filme
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/logar/')
def index(request):
   
    mostrar_filme = Filme.objects.filter(filme_criado_por=request.user)
    print(mostrar_filme)
    paginator = Paginator(mostrar_filme, 5) 
    page = request.GET.get('p')
    mostrar_filme = paginator.get_page(page)
    print(request.user)
    return render(request, 'filmes/index.html', {'mostrar_filme':mostrar_filme})

@login_required(login_url='/auth/logar/')
def cadastrar_filme(request):
    if request.method == "GET":
        return render(request, 'filmes/cadastrar_filme.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        ano = request.POST.get('ano')
        assistido = request.POST.get('assistido')
        genero = request.POST.get('genero')
        classificacao = request.POST.get('classificacao')
        sinopse = request.POST.get('sinopse')

        if assistido == "t":
            assistido = True
        else:
            assistido = False
        
        filme = Filme(nome=nome, ano=ano, assistido=assistido, genero=genero, 
                classificacao=classificacao, sinopse=sinopse, filme_criado_por=request.user)

        filme.save()
    
        return redirect('/filme/')


# função que serve para ver um filme
@login_required(login_url='/auth/logar/')
def filme_unico(request, id):
    filme = get_object_or_404(Filme, pk=id)
    return render(request, 'filmes/filme_unico.html', {'filme_unico':filme})  

@login_required(login_url='/auth/logar/')
def editar_filme(request, id):
    if request.method == "GET":
        atualiza = Filme.objects.get(id=id)
        return render(request, 'filmes/editar_filme.html', {'atualiza':atualiza})
    if request.method == "POST":
        atualiza = Filme.objects.get(id=id)
        nome = request.POST.get('nome')
        ano = request.POST.get('ano')
        assistido = request.POST.get('assistido')
        genero = request.POST.get('genero')
        classificacao = request.POST.get('classificacao')
        sinopse = request.POST.get('sinopse')

        if assistido == "t":
            assistido = True
        else:
            assistido = False

        atualiza.nome = nome
        atualiza.ano = ano
        atualiza.assistido = assistido
        atualiza.genero = genero
        atualiza.classificacao = classificacao
        atualiza.sinopse = sinopse

        atualiza.save()
        return redirect('/filme/')

@login_required(login_url='/auth/logar/')
def excluir_filme(request, id):
    filme = get_object_or_404(Filme, pk=id)
    filme.delete()
    return redirect('/filme')


