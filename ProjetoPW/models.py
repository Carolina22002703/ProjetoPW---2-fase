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

class Quizz(models.Model):
    utilizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="utilizador")
    pergunta = models.CharField(max_length=50)
    resposta = models.CharField(max_length=50)
    numero = models.IntegerField()

    def __str__(self):
        return f"Pergunta {self.id}: {self.pergunta} to {self.resposta}"
