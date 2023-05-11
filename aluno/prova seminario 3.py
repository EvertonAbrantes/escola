from django.db import models

# Create your models here.

from django.db import models
    

    
class alunos(models.Model):

    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    matricula = models.CharField(max_length=50)
    datanascimento = models.DateField(max_length=20)

