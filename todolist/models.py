from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)
    date = models.DateField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
