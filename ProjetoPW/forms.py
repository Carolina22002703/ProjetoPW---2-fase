from django import forms
from .models import Usuario



class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "apelido", "telefone", "email", "dataNascimento"]


