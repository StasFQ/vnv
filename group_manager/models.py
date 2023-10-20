from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    members = models.ManyToManyField(User)
