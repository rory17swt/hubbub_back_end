from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username