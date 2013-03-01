from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WeiboAccount(models.Model):
    access_token = models.CharField(max_length=32)
    user = models.OneToOneField(User)

class RenrenAccount(models.Model):
    access_token = models.CharField(max_length=32)
    user = models.OneToOneField(User)

class FudanAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    user = models.OneToOneField(User)

class FetionAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    user = models.OneToOneField(User)