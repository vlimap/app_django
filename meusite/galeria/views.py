from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Necessario login!')
        return redirect('login')
    fotos = Fotografia.objects.order_by('data').filter(publicada=True)
    return render(request,'galeria/index.html', {"cards" : fotos})

def imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Necessario login!')
        return redirect('login')
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request,'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Necessario login!')
        return redirect('login')
    fotos = Fotografia.objects.order_by('data').filter(publicada=True)
    if "buscar" in request.GET:
        nome_busca = request.GET["buscar"]
        if nome_busca:
            fotos = fotos.filter(nome__icontains = nome_busca)
    return render(request, 'galeria/buscar.html',{"cards": fotos})