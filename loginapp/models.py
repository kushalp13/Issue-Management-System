from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=16,primary_key=True)
    password = models.CharField(max_length=10)
    usertype = models.CharField(max_length=13)

