from django.db import models


# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=100)
    progress = models.CharField(max_length=100, default="In progress")
