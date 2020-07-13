from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField("Date Created", default=datetime.now())
    objects = models.Manager()

    def __str__(self):
        return self.title
