from django.shortcuts import render
from django.urls import path
from . import views

app_name = "quizz"

urlpatterns = [
    path('quizz/', views.quizz_view, name=""),
    path('submit/', views.SubmitTentativa_view, name="enviar"),
    path('pontuacao/', views.pontuacao_view, name="pontuacao"),
]