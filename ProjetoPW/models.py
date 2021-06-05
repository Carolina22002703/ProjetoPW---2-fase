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
    dificuldade = models.CharField(max_length=50, choices=OPCOES)

    def __str__(self):
        return not self.nome + ' ' + self.topico

    def get_perguntas(self):
        return self.pergunta_set.all()

class Pergunta(models.Model):
    textoPergunta = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    criado = models.DateTimeField(auto_now_add="True")

    def __str__(self):
        return str(self.textoPergunta)
    def get_respostas(self):
        return self.resposta_set.all()

class Resposta(models.Model):
    textoResposta = models.CharField(max_length=50)
    correta = models.BooleanField(default=False)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    criado = models.DateTimeField(auto_now_add="True")

    def __str__(self):
        return f"Pergunta: {self.textoPergunta}, Resposta: {self.textoResposta}, Resposta correta {self.correta}"

class Resultados(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    utilizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pontuacao = models.FloatField()

    def __str__(self):
        return str(self.pk)