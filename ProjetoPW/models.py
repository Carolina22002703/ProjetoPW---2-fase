from django.db import models

# Create your models here.
class Quizz(models.Model):
    OPCOES1 =[]
    pergunta1 = models.CharField(max_length=1, choices=OPCOES1)



class Usuario(models.Model):
    nome = models.CharField(max_length=30, null=False)
    apelido = models.CharField(max_length=30, null=False)
    telefone = models.CharField(max_length=9, null=False)
    email = models.EmailField(null=False)
    dataNascimento = models.DateTimeField(null=False)


def __str__(self):
    return self.tituloPergunta[:50]








