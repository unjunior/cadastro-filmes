from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/filme/')
    if request.method == "GET":
        return render(request, 'autenticacao/cadastro.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        usuario = User.objects.filter(username=nome) | User.objects.filter(email=email)
        if usuario.exists():
            #print('Ja existe usuário ou email cadastrados')
            messages.add_message(request, constants.ERROR, 'Ja existe usuário ou email cadastrado')
            return redirect('/auth/cadastro')
        
        if len(senha.strip()) < 6:
            messages.add_message(request, constants.WARNING, 'Digite uma senha com no mínino 4 caracteres')
            return redirect('/auth/cadastro')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro')
        
        usuario = User.objects.create_user(username=nome,
                                            email=email,
                                            password=senha)
        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
        return redirect('/auth/logar/')


def logar(request):
    
    if request.user.is_authenticated:
        return redirect('/filme/')
    if request.method == "GET":
        return render(request, 'autenticacao/logar.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(request, username=nome, password=senha)
        if usuario:
            auth.login(request, usuario)
            return redirect('/filme/')
        else:
            messages.add_message(request, constants.WARNING, 'Usuário ou senha incorretos')
            return redirect('/auth/logar/')

def sair(request):
    auth.logout(request)
    return redirect('/auth/logar/')