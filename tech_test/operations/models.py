from django.db import models
from django.urls import reverse


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=1, null=True)
    date_of_birth = models.CharField(max_length=10)
    industry = models.TextField(null=True)
    salary = models.FloatField(null=True)
    years_of_experience = models.IntegerField(null=True)
