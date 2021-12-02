from django.db import models


# Create your models here.
class Tasks(models.Model):
    """Model for Points class"""
    text = models.TextField(max_length=500)
    day = models.TextField(max_length=500)
    reminder = models.BooleanField(default=False)
