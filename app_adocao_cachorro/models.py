from django.db import models

class Doador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Cachorro(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    idade = models.IntegerField()
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    descricao = models.TextField()
    imagem_url = models.URLField(blank=True)

    def __str__(self):
        return self.nome
