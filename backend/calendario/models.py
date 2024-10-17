from django.db import models
from django.contrib.auth.models import User

class Cultura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Bandeja(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Plantio(models.Model):
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)
    bandeja = models.ForeignKey(Bandeja, on_delete=models.CASCADE)
    especie = models.CharField(max_length=100)
    celula = models.CharField(max_length=10)
    produtividade = models.FloatField()
    variedade = models.CharField(max_length=100)
    data_plantio = models.DateField()
    data_colheita = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cultura.nome} - {self.variedade}"
    
class Notificacao(models.Model):
    plantio = models.ForeignKey(Plantio, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255)
    enviada = models.BooleanField(default=False)
    data_notificacao = models.DateTimeField()

    def __str__(self):
        return f"Notificação para {self.plantio.cultura.nome} em {self.data_notificacao}"


        