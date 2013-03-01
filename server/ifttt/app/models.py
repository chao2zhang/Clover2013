from account_models import *
from django.db import models
from django.contrib.auth.models import User

class Trigger(models.Model):
    kind = models.CharField(max_length=12)
    source = models.CharField(max_length=32)
    content = models.CharField(max_length=140)
    updated_at = models.DateTimeField(auto_now=True)

class Action(models.Model):
    kind = models.CharField(max_length=12)
    source = models.CharField(max_length=32)
    destination = models.CharField(max_length=32)
    content = models.CharField(max_length=140)

class Pending(models.Model):
    action = models.ForeignKey(Action, related_name="pendings")
    done = models.BooleanField()
    content = models.CharField(max_length=140)

class Task(models.Model):
    user = models.ForeignKey(User, related_name="tasks")
    trigger = models.ForeignKey(Trigger, related_name="tasks")
    action = models.ForeignKey(Action, related_name="tasks")
    parent = models.ForeignKey("self", blank=True, related_name="children")