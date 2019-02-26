from django.db import models

# Create your models here.
from django.db.models.functions import datetime
from pytz import unicode

class Contest(models.Model):
    task_1_id = models.IntegerField(default=-1)
    task_2_id = models.IntegerField(default=-1)
    task_3_id = models.IntegerField(default=-1)
    task_4_id = models.IntegerField(default=-1)
    task_5_id = models.IntegerField(default=-1)
    task_6_id = models.IntegerField(default=-1)
    duraction = models.IntegerField(default=-1)
    author = models.CharField(max_length=100, default="People")
    team_size = models.IntegerField(default=4)
    dateST = models.DateTimeField(default=datetime.timezone.now(), blank=True)
    dateED = models.DateTimeField(default=datetime.timezone.now(), blank=True)
