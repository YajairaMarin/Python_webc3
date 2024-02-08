from django.db import models


# Create your models here.
class Libro(models.Model):
    Titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    resumen = models.TextField()


def _str_(self):
  return self.titulo
