#coding:utf8
from django.db import models
from django.contrib.auth.models import User
from utils import KIND2STATIC
from account import binded_account

ACTION_KINDS = (
    "weibo-post",
    "renren-post",
    "fudan-send2me",
    "fudan-send2others",
    "fetion-send2me",
    "fetion-send2others",
)

def _add2action(action):
    action['kind'] = action['action_kind'].partition('-')[0]
    action['static'] = KIND2STATIC[action['kind']]
    return action

ACTION_DETAILS = map(_add2action, (
    {'title': u'发表一条微博', 'action_kind': 'weibo-post', 'require_password': False},
    {'title': u'发表一条人人状态', 'action_kind': 'renren-post', 'require_password': False},
    {'title': u'发送复旦邮件给我', 'action_kind': 'fudan-send2me', 'require_password': False},
    {'title': u'发送复旦邮件给别人', 'action_kind': 'fudan-send2others', 'require_password': True},
    {'title': u'发送飞信给我', 'action_kind': 'fetion-send2me', 'require_password': False},
    {'title': u'发送飞信给别人', 'action_kind': 'fetion-send2others', 'require_password': True},
    )
)

class Action(models.Model):
    kind = models.CharField(max_length=12)
    source = models.CharField(max_length=32, null=True)
    destination = models.CharField(max_length=32, null=True)
    content = models.CharField(max_length=600) #pre-formatted string
    def static(self):
        return KIND2STATIC[self.kind.partition('-')[0]]
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
    actions = filter(lambda detail: binded_account(user, kind=detail['kind'], require_password=detail['require_password']), ACTION_DETAILS)
    return actions