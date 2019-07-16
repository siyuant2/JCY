from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    uin = models.IntegerField()
    major = models.CharField(max_length=20)
    interest = models.CharField(max_length=15)
    skill = models.CharField(max_length=15)

    def __str__(self):
        return self.name
