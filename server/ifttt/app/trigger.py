from django.db import models
from django.contrib.auth.models import User
from account import binded_account
from utils import KIND2ACCOUNT, KIND2STATIC

TRIGGER_KINDS = (
    'weibo-new',
    'renren-new',
    'fudan-new',
    )

def _add2trigger(trigger):
    trigger['kind'] = trigger['trigger_kind'].partition('-')[0]
    trigger['static'] = KIND2STATIC[trigger['kind']]
    return trigger

TRIGGER_DETAILS = map(_add2trigger, (
    {'title': 'A new post from Weibo', 'trigger_kind': 'weibo-new', 'require_password': False},
    {'title': 'A new post from Renren', 'trigger_kind': 'renren-new', 'require_password': False},
    {'title': 'A new mail from FudanMail', 'trigger_kind': 'fudan-new', 'require_password': True},
    )
)

class Trigger(models.Model):
    kind = models.CharField(max_length=12)
    source = models.CharField(max_length=32, null=True)
    content = models.CharField(max_length=140, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def static(self):
        return KIND2STATIC[self.kind.partition('-')[0]]
    def clone(self):
        trigger = Trigger.objects.get(pk=self.id)
        trigger.id = None
        trigger.save()
        return trigger

def active_triggers(user):
    triggers = filter(lambda detail: binded_account(user, kind=detail['kind'], require_password=detail['require_password']), TRIGGER_DETAILS)
    return triggers
