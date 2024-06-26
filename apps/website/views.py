from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#@login_required
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    return render(request, 'website_template/index.html', {'user':request.user})
