from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):
    nome = models.CharField(max_length=30)
    ano = models.IntegerField()
    assistido = models.BooleanField(default=False)
    
    GENERO_CHOICES = (
        ("AC", "Ação"),
        ("AV", "Aventura"),
        ("CO", "Comédia"),
        ("DO", "Documentário"),
        ("DR", "Drama"),
        ("FI", "Ficção Científica"),
        ("MU", "Musical"),
        ("RO", "Romance"),
        ("SU", "Suspense"),
        ("TE", "Terror")
    )

    CLASSIFICACAO_CHOICES = (
        ("L", "Livre"),
        ("10", "10 anos"),
        ("14", "14 anos"),
        ("16", "16 anos"),
        ("18", "18 anos")
    )
    genero = models.CharField(max_length=15, choices=GENERO_CHOICES, blank=False, null=False)
    classificacao = models.CharField(max_length=5, choices=CLASSIFICACAO_CHOICES, blank=False, null=False)
    sinopse = models.TextField()

    def __str__(self):
        return self.nome
    
    filme_criado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)