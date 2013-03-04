from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from oauth.weibo import *
from oauth.renren import *
from utils import KIND2ACCOUNT, KIND2USTATIC, KIND2STATIC

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

ACCOUNT_DETAILS = (
    {'title':'Renren', 'description':'OAuth 2.0 on Renren', 'kind':'renren'},
    {'title':'Weibo', 'description':'OAuth 2.0 on Renren', 'kind':'weibo'},
    {'title':'Fudan Mail', 'description':'If you set up your address, you can receive an email from system. If you set up your password, system can use your account to send a fudan mail to others', 'kind':'fudan'},
    {'title':'Fetion', 'description':'If you set up your phone number, you can receive a fetion message from system. If you set up your password, system can use your fetion to send a message mail to others', 'kind':'fetion'},
)

def binded_accounts(user):
    return filter(lambda name: hasattr(user, name.lower()), ACCOUNT_NAMES)

def binded_account(user, kind=None, name=None, require_password=False):
    if kind:
        name = KIND2ACCOUNT[kind]
    name = name.lower()
    if name:
        return hasattr(user, name) and getattr(user, name).password if require_password else hasattr(user, name)
    return False

def binds(user):
    details = list(ACCOUNT_DETAILS)
    for a in details:
        a['account'] = KIND2ACCOUNT[a['kind']]
        a['static'] = KIND2STATIC[a['kind']] if binded_account(user, a['kind']) else KIND2USTATIC[a['kind']]
        a['url'] = eval(a['account']).url()
    return details

class WeiboAccount(models.Model):
    access_token = models.CharField(max_length=32)
    user = models.OneToOneField(User)
    @staticmethod
    def url():
        return Weibo.auth_uri()


class RenrenAccount(models.Model):
    access_token = models.CharField(max_length=32)
    user = models.OneToOneField(User)
    @staticmethod
    def url():
        return Renren.auth_uri()

class FudanAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=True)
    user = models.OneToOneField(User)
    @staticmethod
    def url():
        return reverse('bind_fudan')

class FetionAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=True)
    user = models.OneToOneField(User)
    @staticmethod
    def url():
        return reverse('bind_fetion')
