from django.db import models


class TaskModel(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=250)
    state = models.IntegerField(default=0)

