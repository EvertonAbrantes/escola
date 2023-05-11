from django.db import models

# Create your models here.
class detalhedisciplina(models.Model):

    cursocodigo = models.SmallIntegerField()
    disciplinacodigo = models.SmallIntegerField()


