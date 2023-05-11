from django.db import models

# Create your models here.
class professor(models.Model):

    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    registro = models.CharField(max_length=100)
    
