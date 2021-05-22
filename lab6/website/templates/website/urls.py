from website.views import sobre_page_view
from django.shortcuts import render
from . import views
from django.urls import path

app_name = href = "{% url 'website:home' %}"

# determinar as três rotas das três pastas
urlpatterns = {
    path('home', views.home_page_view, name='home'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('outraPagina', views.outraPagina_page_view, name='outraPagina')
}
