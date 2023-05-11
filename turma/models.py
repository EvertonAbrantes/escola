from django.db import models

# Create your models here.
from django.db import models

class turma(models.Model):

    codigo = models.SmallIntegerField()
    cursocodigo = models.SmallIntegerField()

