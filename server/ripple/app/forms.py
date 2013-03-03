from django import forms
from django.forms import widgets
from action import Action
from trigger import Trigger
from task import Task
from account import FudanAccount, FetionAccount

class FudanAccountForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=16, required=False, widget=widgets.PasswordInput)
    def save(self, user):
        fa, created = FudanAccount.objects.get_or_create(user=user, username=self.cleaned_data['username'])
        fa.password = self.cleaned_data['password']
        fa.save()

class FetionAccountForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=16, required=False, widget=widgets.PasswordInput)
    def save(self, user):
        fa, created = FetionAccount.objects.get_or_create(user=user, username=self.cleaned_data['username'])
        fa.password = self.cleaned_data['password']
        fa.save()


class TaskForm(forms.Form):
    trigger_kind = forms.CharField(max_length=12, widget=widgets.HiddenInput)
    trigger_source = forms.CharField(max_length=32, required=False)
    trigger_tag = forms.CharField(max_length=140, required=False)
    
    action_kind = forms.CharField(max_length=12, widget=widgets.HiddenInput)
    action_source = forms.CharField(max_length=32, required=False)
    action_destination = forms.CharField(max_length=32, required=False)
    action_content = forms.CharField(max_length=140)

    description = forms.CharField(max_length=140)
    parent = forms.IntegerField(min_value=0, widget=widgets.HiddenInput, required=False)

    def save(self, user):
        d = self.cleaned_data
        trigger = Trigger(kind=d['trigger_kind'], source=d['trigger_source'], content=d['trigger_tag'])
        trigger.save()
        action = Action(kind=d['action_kind'], source=d['action_source'], destination=d['action_destination'], content=d['action_content'])
        action.save()
        task = Task(user=user, description=d['description'], parent=d['parent'], trigger=trigger, action=action)
        task.save()
        return task

class TaskEditForm(TaskForm):
    id = forms.IntegerField(min_value=0, widget=widgets.HiddenInput)
    def save(self, user):
        d = self.cleaned_data
        task = Task.objects.get(pk=d['id'])
        task.description=d.get('description')
        task.save()
        trigger = Trigger.objects.get(pk=task.trigger.id)
        trigger.source=d.get('trigger_source')
        trigger.content=d.get('trigger_content')
        trigger.save()
        action = Action.objects.get(pk=task.action.id)
        action.source=d.get('action_source')
        action.destination=d.get('action_destination')
        action.content=d.get('action_content')
        action.save()
        return task
