from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request, 
            username=username,
            password=password
        )
        if usuario is not None:
            login(request, usuario)
            messages.success(request, "Login efetuado com sucesso!")
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios_template/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')

