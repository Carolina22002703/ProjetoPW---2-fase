from django.shortcuts import render
import datetime


def home_page_view(request):
    lista = ["HTML", "CSS", "Python", "Django"]
    context = {
        'agora': datetime.datetime.now(),
        'lista': lista,
    }
    return render(request, 'website/home.html', context)

def sobre_page_view(request):
    return render(request, 'website/sobre.html')


def outraPagina_page_viwe(request):
    return render(request, 'website/outraPagina.html')