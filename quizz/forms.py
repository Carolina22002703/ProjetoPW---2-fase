from django import forms
from django.forms import ModelForm
from quizz.models import Quizz, Pergunta
from django.db import models

class NovoQuizzFormulario (ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

class NovaPerguntaFormulario:
    class Meta:
        model = Quizz
        fields = '__all__'
