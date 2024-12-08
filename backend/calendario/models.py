from django.db import models
from django.contrib.auth.models import User

class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Cultura(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Bandeja(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Plantio(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, 
                               null=True, blank=True)
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE, 
                                null=True, blank=True)
    bandeja = models.ForeignKey(Bandeja, on_delete=models.CASCADE, 
                                null=True, blank=True)
    especie = models.CharField(max_length=100)
    celula = models.CharField(max_length=10)
    variedade = models.CharField(max_length=100)
    data_plantio = models.DateField()
    data_colheita = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    dicas = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('cidade', 'cultura', 'bandeja', 'especie', 
                           'celula', 'variedade')
    
    def __str__(self):
        return f"{self.cultura.nome} - {self.variedade}"


class Notificacao(models.Model):
    plantio = models.ForeignKey(Plantio, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255)
    enviada = models.BooleanField(default=False)
    data_notificacao = models.DateTimeField()

    def __str__(self):
        return f"Notificação para {self.plantio.cultura.nome} em {self.data_notificacao}"


class Evento(models.Model):
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    descricao = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        