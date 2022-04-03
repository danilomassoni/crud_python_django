from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.forms import FilmesForms
from app.models import Filmes


# CRIAMOS AQUI AS FUNÇÕES PARA O NOSSO SISTEMA FUNCIONAR. 

def home(request):
    '''FUNÇÃO PARA CRIARMOS NOSSA HOME E RECEBERMOS OS VALORES INSERIDOS NO BANCO'''
    data = {}
    data['db'] = Filmes.objects.all()
    return render(request, 'index.html', data)

def form(request):
    '''CRIAMOS NOSSO FORMULÁRIO COM ESSA FUNÇÃO'''
    data = {}
    data['form'] = FilmesForms()
    return render(request, 'form.html', data)

def create(request):
    '''COM ESSA FUNÇÃO CRIAMOS UMA REQUISIÇÃO E ENVIAMOS AO BANCO. DEPOIS RETORNAMOS PARA A PÁGINA HOME'''
    form = FilmesForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    '''AQUI TEREMOS AS VISUALIZAÇÕES DOS CADASTROS'''
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    '''VAMOS EDITAR AS INSERÇÕES NO BANCO ATRAVÉS DESSA FUNÇÃO'''
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    data['form'] = FilmesForms(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    '''VAMOS ATUALIZAR OS ITENS INSERIDOS EM NOSSOS CÓDIGOS'''
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    form = FilmesForms(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    '''FUNÇÃO PARA DELETAR OS ITENS'''
    db = Filmes.objects.get(pk=pk)
    db.delete()
    return redirect('home')