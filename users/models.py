from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone=models.CharField(max_length=15,blank=True)
    credit_score=models.IntegerField(default=650)
    annual_income=models.FloatField(default=0)
    def __str__(self):
        return self.username
