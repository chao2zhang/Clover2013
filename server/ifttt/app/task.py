from django.db import models
from django.contrib.auth.models import User
from trigger import Trigger
from action import Action

class Task(models.Model):
    user = models.ForeignKey(User, related_name="tasks")
    trigger = models.ForeignKey(Trigger, related_name="tasks")
    action = models.ForeignKey(Action, related_name="tasks")
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children")
    description = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)