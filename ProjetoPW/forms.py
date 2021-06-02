from django import forms
from .models import Usuario
from django.forms import ModelForm


class UsuarioFormulario(ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "apelido", "telefone", "email", "dataNascimento"]
