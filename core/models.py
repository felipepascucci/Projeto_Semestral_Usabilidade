from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=125)
    dt_nasc = models.DateField
    email = models.CharField(max_length=125)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    
    