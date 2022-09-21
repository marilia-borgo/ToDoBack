from django.db import models

# Create your models here.

class Tasks(models.Model):
    titulo=models.CharField(max_length=128, unique=True)
    projeto=models.TextField(max_length=128)
    dueTo=models.DateField()
    feito = models.BooleanField(default=False)

