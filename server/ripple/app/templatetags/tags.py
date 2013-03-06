from django.contrib.auth.models import User
from django import template
from app.account import binded_accounts, ACCOUNT_NAMES, UNAUTHENTICATED_ACCOUNT_NAMES

register = template.Library()

@register.simple_tag(name='count_accounts')
def count_accounts(user):
    return len(binded_accounts(user))

@register.simple_tag(name='total_accounts') 
def total_accounts():
    return len(ACCOUNT_NAMES + UNAUTHENTICATED_ACCOUNT_NAMES)

@register.simple_tag(name='count_tasks')
def count_tasks(user):
    return user.tasks.count()

@register.inclusion_tag('tags/_trigger_grid.html')
def trigger_grid(trigger):
    return {'trigger': trigger}

@register.inclusion_tag('tags/_action_grid.html')
def action_grid(action):
    return {'action': action}

@register.inclusion_tag('tags/_task_grid.html')
def task_grid(task):
    return {'task': task}

@register.inclusion_tag('tags/_task_line.html')
def task_line(task):
    return {'task': task}

@register.inclusion_tag('tags/_trigger_action_line.html')
def trigger_action_line(task):
    return {'task': task}

@register.inclusion_tag('tags/_bind_grid.html')
def bind_grid(bind):
    return {'bind': bind}

@register.inclusion_tag('tags/_bind_item.html')
def bind_item(bind):
    return {'bind': bind}

@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})

from app.action import ACTION_DETAILS
from app.trigger import TRIGGER_DETAILS

@register.filter
def trigger_title(trigger):
    print trigger.kind
    for detail in TRIGGER_DETAILS:
        if trigger.kind == detail['trigger_kind']:
            return detail['title']

@register.filter
def action_title(action):
    for detail in ACTION_DETAILS:
        if action.kind == detail['action_kind']:
            return detail['title']