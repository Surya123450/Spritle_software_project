from django.db import models
from django.contrib.auth.models import AbstractUser

class Master(AbstractUser):
    # Master-specific fields go here

    def __str__(self):
        return self.username

class Student(AbstractUser):
    # Student-specific fields go here

    def __str__(self):
        return self.username
