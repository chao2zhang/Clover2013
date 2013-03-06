# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from account import binded_account
from utils import account_with_kind, static_with_kind

def proc_trigger(trigger):
    trigger['kind'] = trigger['trigger_kind'].partition('-')[0]
    trigger['static'] = static_with_kind(trigger['kind'])
    return trigger

TRIGGER_DETAILS = map(proc_trigger, (
    {'title': u'当收到一条微博', 'trigger_kind': 'weibo-new', 'require_password': False},
    {'title': u'当收到一条人人状态', 'trigger_kind': 'renren-new', 'require_password': False},
    {'title': u'当收到一封复旦邮件', 'trigger_kind': 'fudan-new', 'require_password': True},
    {'title': u'今日有雨雪', 'trigger_kind': 'weather-rain', 'require_password': False},
    {'title': u'今日温度大于', 'trigger_kind': 'weather-larger', 'require_password': False},
    {'title': u'今日温度小于', 'trigger_kind': 'weather-smaller', 'require_password': False},
    {'title': u'当股票价格大于', 'trigger_kind': 'stock-larger', 'require_password': False},
    {'title': u'当股票价格小于', 'trigger_kind': 'stock-smaller', 'require_password': False},
    )
)

class Trigger(models.Model):
    kind = models.CharField(max_length=12)
    source = models.CharField(max_length=32, null=True)
    content = models.CharField(max_length=140, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def static(self):
        return static_with_kind(self.kind.partition('-')[0])
    def clone(self):
        trigger = Trigger.objects.get(pk=self.id)
        trigger.id = None
        trigger.save()
        return trigger

def active_triggers(user):
    triggers = filter(lambda detail: binded_account(user, kind=detail['kind'], require_password=detail['require_password']), TRIGGER_DETAILS)
    return triggers
