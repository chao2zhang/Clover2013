# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from utils import static_with_kind, static_unbind_with_kind
from account import binded_account

def proc_action(action):
    action['kind'] = action['action_kind'].partition('-')[0]
    action['static'] = static_with_kind(action['kind'])
    action['static_unbind'] = static_unbind_with_kind(action['kind'])
    return action

ACTION_DETAILS = map(proc_action, (
    {'title': u'发表一条微博', 'action_kind': 'weibo-post', 'require_password': False},
    {'title': u'发送一篇新浪博客', 'action_kind': 'sinablog-post', 'require_password': False},
    {'title': u'发表一条人人状态', 'action_kind': 'renren-post', 'require_password': False},
    {'title': u'发送复旦邮件给我', 'action_kind': 'fudan-send2me', 'require_password': False},
    {'title': u'发送复旦邮件给别人', 'action_kind': 'fudan-send2others', 'require_password': True},
    {'title': u'发送网易邮件给我', 'action_kind': 'wangyi-send2me', 'require_password': False},
    {'title': u'发送网易邮件给别人', 'action_kind': 'wangyi-send2others', 'require_password': True},
    {'title': u'发送飞信给我', 'action_kind': 'fetion-send2me', 'require_password': False},
    {'title': u'发送飞信给别人', 'action_kind': 'fetion-send2others', 'require_password': True},
    )
)

class Action(models.Model):
    kind = models.CharField(max_length=12)
    destination = models.CharField(max_length=32, null=True)
    content = models.CharField(max_length=600) #pre-formatted string
    def static(self):
        return static_with_kind(self.kind.partition('-')[0])
    def static_unbind(self):
        return static_unbind_with_kind(self.kind.partition('-')[0])
    def clone(self):
        action = Action.objects.get(pk=self.id)
        action.id = None
        action.save()
        return action

class Pending(models.Model):
    action = models.ForeignKey(Action, related_name="pendings")
    done = models.BooleanField()
    content = models.CharField(max_length=600) #formatted string

def active_actions(user):
    actions = ACTION_DETAILS
    for detail in actions:
        detail['active'] = binded_account(user, kind=detail['kind'], require_password=detail['require_password'])
    return actions