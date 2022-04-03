from django.db import models

# Create your models here.

class Filmes(models.Model):
    '''AQUI CRIAMOS NOSSO BANCO DE DADOS, INFORMANDO QUAIS CAMPOS VAMOS PEGAR COM O USUÁRIO'''
    filme = models.CharField(max_length=150)
    genero = models.CharField(max_length=100)
    duracao = models.IntegerField()
    data_lancamento = models.DateField()
    diretor = models.CharField(max_length=150)
    principais_artistas = models.TextField()

