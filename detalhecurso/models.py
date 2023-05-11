from django.db import models

# Create your models here.
class detalhecurso(models.Model):

    cursocodigo = models.SmallIntegerField()
    turmacodigo = models.SmallIntegerField()
