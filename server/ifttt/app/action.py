from django.db import models
from django.contrib.auth.models import User
from utils import KIND2STATIC
from account import binded_account

ACTION_KINDS = (
    "weibo-post",
    "weibo-repost",
    "renren-post",
    "renren-repost",
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
    {'title': 'Post to Weibo', 'action_kind': 'weibo-post', 'require_password': False},
    {'title': 'Repost to Weibo', 'action_kind': 'weibo-repost', 'require_password': False},
    {'title': 'Post to Renren', 'action_kind': 'renren-post', 'require_password': False},
    {'title': 'Repost to Renren', 'action_kind': 'renren-repost', 'require_password': False},
    {'title': 'Send a Fudan mail to me', 'action_kind': 'fudan-send2me', 'require_password': False},
    {'title': 'Send a Fudan mail to others', 'action_kind': 'fudan-send2others', 'require_password': True},
    {'title': 'Send a Fetion message to me', 'action_kind': 'fetion-send2me', 'require_password': False},
    {'title': 'Send a Fetion message to others', 'action_kind': 'fetion-send2others', 'require_password': True},
    )
)

class Action(models.Model):
    kind = models.CharField(max_length=12)
    source = models.CharField(max_length=32)
    destination = models.CharField(max_length=32)
    content = models.CharField(max_length=140) #pre-formatted string

class Pending(models.Model):
    action = models.ForeignKey(Action, related_name="pendings")
    done = models.BooleanField()
    content = models.CharField(max_length=140) #formatted string

def active_actions(user):
    actions = filter(lambda detail: binded_account(user, kind=detail['kind'], require_password=detail['require_password']), ACTION_DETAILS)
    return actions