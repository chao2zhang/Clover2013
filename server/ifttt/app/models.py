from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WeiboAccount(models.Model):
    access_token = models.CharField(max_length=32)
    user = models.OneToOneField(User)