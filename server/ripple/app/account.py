# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from oauth.weibo import *
from oauth.renren import *
from utils import account_with_kind, static_unbinded_with_kind, static_with_kind

ACCOUNT_NAMES = (
    "WeiboAccount",
    "RenrenAccount",
    "FudanAccount",
    "FetionAccount",
    "WangyiAccount",
    "SinablogAccount",
)

UNAUTHENTICATED_ACCOUNT_NAMES = (
    "WeatherAccount",
    "StockAccount",
)

ACCOUNT_DETAILS = (
    {'title':u'人人网', 'kind':'renren'},
    {'title':u'新浪微博', 'kind':'weibo'},
    {'title':u'新浪博客', 'kind':'sinablog'},
    {'title':u'飞信', 'kind':'fetion'},
    {'title':u'复旦邮箱', 'kind':'fudan'},
    {'title':u'网易', 'kind':'wangyi'},
)

UNAUTHENTICATED_ACCOUNT_DETAILS = (
    {'title':u'天气', 'kind':'weather'},
    {'title':u'股票', 'kind':'stock'},
)

def binded_accounts(user):
    return filter(lambda name: hasattr(user, name.lower()), ACCOUNT_NAMES) + UNAUTHENTICATED_ACCOUNT_NAMES

def binded_account(user, kind, require_password=False):
    name = account_with_kind(kind)
    if name in UNAUTHENTICATED_ACCOUNT_NAMES: return True
    name = name.lower()
    return hasattr(user, name) and getattr(user, name).password if require_password else hasattr(user, name)

def binds(user):
    details = []
    for d in ACCOUNT_DETAILS:
        d['account'] = account_with_kind(d['kind'])
        d['static'] = static_with_kind(d['kind']) if binded_account(user, d['kind']) else static_unbinded_with_kind(d['kind'])
        d['url'] = eval(d['account']).url()
        details.append(d)
    for d in UNAUTHENTICATED_ACCOUNT_DETAILS:
        d['static'] = static_with_kind(d['kind'])
        details.append(d)
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

class WangyiAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=True)
    user = models.OneToOneField(User)
    @staticmethod
    def url():
        return reverse('bind_wangyi')

class SinablogAccount(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16, null=True)
    user = models.OneToOneField(User)
    @staticmethod
    def url():
        return reverse('bind_sinablog')
