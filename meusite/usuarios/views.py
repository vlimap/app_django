from django.shortcuts import render, redirect
from usuarios.forms import FormLogin, FormCadastro
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib import messages

def login(request):
    form = FormLogin()
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']

            # Primeiro, verificar se o usuário existe
            if not User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário não existe!')
                return redirect('login')

            # Se o usuário existir, tentar autenticar
            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Seja bem vindo, {nome}!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha errada!')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = FormCadastro()
    if request.method == 'POST':
        form = FormCadastro(request.POST)
        if form.is_valid():
            senha = form.cleaned_data['senha']
            confirmar_senha = form.cleaned_data['confirmar_senha']
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']

            if senha != confirmar_senha:
                messages.error(request,'As senhas não são iguais!')
                return redirect('cadastro')

            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuario já existe!')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request,f'{nome} cadastrado!')
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

