from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Usuario
#from .models import  Quizz, Resposta, Pergunta
from .forms import UsuarioFormulario
#from .forms QuizzFormulario, PerguntaFormulario


# Create your views here.

# Mapa
def mapa_page_view(request):
    return render(request, 'ProjetoPW/mapa.html')


# Informacao
def informcao_page_view(request):
    return render(request, 'ProjetoPW/informacao.html')


# Formulário
def formulario_page_view(request):
    return render(request, 'ProjetoPW/formulario.html')


# Index
def index_page_view(request):
    return render(request, 'ProjetoPW/index.html')


# Mirazur
def mirazurIntroducao_page_view(request):
    return render(request, 'ProjetoPW/mirazurIntroducao.html')


def mirazurCozinha_page_view(requeste):
    return render(requeste, 'ProjetoPW/mirazurCozinha.html')


def mirazurPinteresse_page_view(requeste):
    return render(requeste, 'ProjetoPW/mirazurPinteresse.html')


# Celler
def cellerIntroducao_page_view(request):
    return render(request, 'ProjetoPW/cellerIntroducao.html')


def cellerCozinha_page_view(requeste):
    return render(requeste, 'ProjetoPW/cellerCozinha.html')


def cellerPinteresse_page_view(requeste):
    return render(requeste, 'ProjetoPW/cellerPinteresse.html')


# Noma
def nomaIntroducao_page_view(request):
    return render(request, 'ProjetoPW/nomaIntroducao.html')


def nomaCozinha_page_view(requeste):
    return render(requeste, 'ProjetoPW/nomaCozinha.html')


def nomaPinteresse_page_view(request):
    return render(request, 'ProjetoPW/nomaPinteresse.html')


#Quizz

def quizz_page_view(request):
    context = {'ProjetoPW': Quizz.objects.all()}
    return render (request, 'ProjetoPW/quizz.html', context) #, context


# Contacto
def contacto_page_view(request):
    context = {'ProjetoPW': Usuario.objects.all()}
    return render(request, 'ProjetoPW/contacto.html', context)


def novo_contacto_view(request):
    form = UsuarioFormulario(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ProjetoPW:contacto'))

    context = {'form': form}

    return render(request, 'ProjetoPW/listar.html', context)


def edita_contacto_view(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    form = UsuarioFormulario(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ProjetoPW:contacto'))

    context = {'form': form, 'usuario_id': usuario_id}
    return render(request, 'ProjetoPW/edita.html', context)


def apaga_contacto_view(request, usuario_id):
    Usuario.objects.get(id=usuario_id.delete())
    return HttpResponseRedirect(reverse('ProjetoPW:contacto'))
