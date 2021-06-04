from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30, null=False)
    apelido = models.CharField(max_length=30, null=False)
    telefone = models.CharField(max_length=9, null=False)
    email = models.EmailField(null=False)
    dataNascimento = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.nome} {self.apelido} {self.telefone} {self.email} {self.dataNascimento}"

"""
class Quiz (models.Model):
    OPCOES = [
        ('fácil','fácil'),
        ('médio','médio'),
        ('dificil','dificil')
    ]
    nome = models.CharField(max_length=50)
    topico = models.CharField(max_length=100)
    numeroQuestoes = models.IntegerField()
    tempo = models.IntegerField(help_text="duração do quizz em minutos")
    pontuacaoParaPassar = models.IntegerField(help_text="pontos requeritos em %")
    dificuldade = models.CharField(max_length=, choices=OPCOES)

    def __str__(self):
        return not self.nome + ' ' + self.topico

    def get_perguntas(self):
        pass
"""

"""
class Quizz(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.nome

class Pergunta(models.Model):
    textoPergunta = models.CharField(max_length=256)
    publicado = models.BooleanField(default=False)
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE, related_name="perguntas")

    def __str__(self):
        return "{content} - {published}".format(content=self.textoPergunta, published=self.publicado)

class Resposta(models.Model):
    textoResposta = models.CharField(max_length=128)
    correto = models.BooleanField(default=False)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name="respostas")

    def __str__(self):
        return self.textoResposta
"""

"""class Resposta(models.Model):
    textoResposta = models.CharField(max_length=100)
    respostaCorreta = models.BooleanField(default=False)
    utilizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.textoResposta

class Pergunta(models.Model):
    textoPergunta = models.CharField(max_length=100)
    respostas = models.ManyToManyField(Resposta)
    points = models.IntegerField()
    utilizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.textoPergunta

class Quizz(models.Model):
    utilizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    due = models.DateField()
    perguntas = models.ManyToManyField(Pergunta)

    def __str__(self):
        return self.titulo"""


"""class Tentativa(models.Model):
    utilizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    pontos = models.PositiveIntegerField()
    completo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.utilizador

class Tentar(models.Model):
    quiz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    tentativa = models.ForeignKey(Tentativa, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.ForeignKey(Resposta, on_delete=models.CASCADE)

    def __str__(self):
        return self.tentativa.utilizador + '-' + self.resposta.textoResposta"""

