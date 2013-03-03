from django.db import models
from django.contrib.auth.models import User
from utils import KIND2ACCOUNT

ACCOUNT_NAMES = (
    "WeiboAccount",
    "RenrenAccount",
    "FudanAccount",
    "FetionAccount",
)

ACCOUNT_KINDS = (
    "weibo",
    "renren",
    "fudan",
    "fetion",
)

def binded_accounts(user):
    return filter(lambda name: hasattr(user, name.lower()), ACCOUNT_NAMES)

def binded_account(user, kind=None, name=None, require_password=None):
    if kind:
        name = KIND2ACCOUNT[kind]
    name = name.lower()
    if name:
        return hasattr(user, name) and getattr(user, name).password if require_password else hasattr(user, name)
    return False

class WeiboAccount(models.Model):
    access_token = models.CharField(max_length=32)
    user = models.OneToOneField(User)

class RenrenAccount(models.Model):
    access_token = models.CharField(max_length=32)
    user = models.OneToOneField(User)

class FudanAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=True)
    user = models.OneToOneField(User)

class FetionAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=True)
    user = models.OneToOneField(User)
