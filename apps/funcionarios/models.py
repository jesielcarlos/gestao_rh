from django.db import models
from django.db.models.fields import CharField

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome