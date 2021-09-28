from django.db import models
from django.db.models.fields import IntegerField

class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
# Create your models here.
