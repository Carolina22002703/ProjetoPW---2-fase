# Generated by Django 3.2.3 on 2021-06-03 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('apelido', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('dataNascimento', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=50)),
                ('resposta', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('utilizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilizador', to='ProjetoPW.usuario')),
            ],
        ),
    ]
