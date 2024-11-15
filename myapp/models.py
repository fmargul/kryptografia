from django.db import models

class Dictionary(models.Model):
    title = models.CharField(max_length=30)
    definition = models.CharField(max_length=300)
