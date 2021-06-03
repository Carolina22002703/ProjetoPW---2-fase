from django import forms
from .models import Usuario, Quizz



class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "apelido", "telefone", "email", "dataNascimento"]

class QuizzFormulario(forms.ModelForm):
    class Meta:
        model = Quizz
        fields = ["utilizador", "pergunta", "resposta", "numero"]
