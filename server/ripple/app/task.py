# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from trigger import Trigger
from action import Action

class Task(models.Model):
    user = models.ForeignKey(User, related_name="tasks")
    trigger = models.OneToOneField(Trigger)
    action = models.OneToOneField(Action)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children")
    description = models.CharField(max_length=140)
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def get_absolute_url(self):
        return '/tasks/%i/' % self.id

    def clone(self, user):
        action = self.action.clone()
        trigger = self.trigger.clone()
        task = Task(user=user, trigger=trigger, action=action, parent=self, description=self.description, public=self.public)
        task.save()
        parent = task.parent
        while parent:
            parent.count += 1
            parent.save()
            parent = parent.parent
        return task
