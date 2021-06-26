from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Resposta(models.Model):
    textoResposta = models.CharField(max_length=50)
    correta = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.textoResposta

class Pergunta(models.Model):
    textoPergunta = models.CharField(max_length=200)
    respostas = models.ManyToManyField(Resposta)
    pontos = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.textoPergunta

class Quizz (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tituloPergunta = models.CharField(max_length=50)
    data = models.DateTimeField (auto_now_add=True)
    due = models.DateField()
    tentativas = models.PositiveIntegerField()
    tempo = models.PositiveIntegerField()
    perguntas = models.ManyToManyField(Pergunta)

    def __str__(self):
        return self.tituloPergunta


class Tentativa(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.ForeignKey(Resposta, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.user.username + ' - ' + self.resposta.textoResposta
