
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    hobby = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
