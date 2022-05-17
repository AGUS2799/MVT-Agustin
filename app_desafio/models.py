from django.db import models

# Create your models here.
class Integrantes(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_of_birth = models.DateField(max_length=40)