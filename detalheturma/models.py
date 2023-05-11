from django.db import models

# Create your models here.
class detalheturma(models.Model):

    alunocodigo =  models.SmallIntegerField()
    professorcodigo =  models.SmallIntegerField()
    turmacodigo = models.SmallIntegerField()

