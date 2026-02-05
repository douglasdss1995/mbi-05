from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    ativo = models.BooleanField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)