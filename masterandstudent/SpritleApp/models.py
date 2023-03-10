from django.db import models
from django.contrib.auth.models import User

class Calculation(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.IntegerField()
