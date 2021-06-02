from django.shortcuts import render
from django.urls import path

from . import views

app_name = "ProjetoPW"


urlpatterns = [
    #Index
    path('', views.index_page_view, name='index'),

    #Celler
    path('cellerIntroducao', views.cellerIntroducao_page_view, name='cellerIntroducao'),
    path('cellerCozinha', views.cellerCozinha_page_view, name='cellerCozinha'),
    path('cellerPinteresse', views.cellerPinteresse_page_view, name='cellerPinteresse'),

    #Mirazur
    path('mirazurIntroducao', views.mirazurIntroducao_page_view, name='mirazurIntroducao'),
    path('mirazurCozinha', views.mirazurCozinha_page_view, name='mirazurCozinha'),
    path('mirazurPinteresse', views.mirazurPinteresse_page_view, name='mirazurPinteresse'),

    #Noma
    path('nomaIntroducao',views.nomaIntroducao_page_view, name='nomaIntroducao'),
    path('nomaCozinha', views.nomaCozinha_page_view, name='nomaCozinha'),
    path('nomaPinteresse',views.nomaPinteresse_page_view, name='nomaPinteresse'),


    #Contacto
    path('home',views.contacto_page_view, name ='contacto'),
    path('listar/', views.novo_contacto_view, name='listar'),
    path('edita/<int:usuario_id>', views.edita_contacto_view, name="edita"),
    path('apaga/<int:usuario_id>', views.apaga_contacto_view, name="apaga"),
]