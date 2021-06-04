from django import forms
from .models import Usuario
#from .models import Quizz, Resposta, Pergunta


class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "apelido", "telefone", "email", "dataNascimento"]
""" 
class QuizzFormulario(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class' : 'validate'}), required=True)
    due = forms.DateField(widget=forms.TextInput(attrs={'class' : 'detepicker'}), required=True)

    class Meta:
        model = Quizz
        fields = ['titulo', 'due']

class PerguntaFormulario(forms.ModelForm):
    textoPergunta = forms.CharField(widget=forms.TextInput(attrs={'class' : 'validate'}), required=True)
    pontos = forms.IntegerField(max_value=100, min_value=1)

    class Meta:
        model = Pergunta
        fields = ['textoPergunta', 'pontos']

"""

