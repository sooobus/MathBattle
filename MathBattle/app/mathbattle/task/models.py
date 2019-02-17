from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=2000)
    author = models.CharField(max_length=100)
    right_answer = models.CharField(max_length=200)
    type = models.IntegerField()
