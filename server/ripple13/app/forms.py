# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets
from models import *
class WangyiAccountForm(forms.Form):
    username = forms.CharField(max_length=32, label=u'网易邮箱')
    password = forms.CharField(max_length=16, label=u'密码', required=False, widget=widgets.PasswordInput)
    def save(self, user):
        wa, created = WangyiAccount.objects.get_or_create(user=user)
        wa.username = self.cleaned_data['username']
        wa.password = self.cleaned_data['password']
        wa.save()

class SinablogAccountForm(forms.Form):
    username = forms.CharField(max_length=32, label=u'新浪博客用户名')
    password = forms.CharField(max_length=16, label=u'密码', required=False, widget=widgets.PasswordInput)
    def save(self, user):
        wa, created = SinablogAccount.objects.get_or_create(user=user)
        wa.username = self.cleaned_data['username']
        wa.password = self.cleaned_data['password']
        wa.save()

class FudanAccountForm(forms.Form):
    username = forms.CharField(max_length=32, label=u'复旦邮箱')
    password = forms.CharField(max_length=16, label=u'密码', required=False, widget=widgets.PasswordInput)
    def save(self, user):
        fa, created = FudanAccount.objects.get_or_create(user=user)
        fa.username = self.cleaned_data['username']
        fa.password = self.cleaned_data['password']
        fa.save()

class FetionAccountForm(forms.Form):
    username = forms.CharField(max_length=32, label=u'飞信帐号')
    password = forms.CharField(max_length=16, label=u'密码', required=False, widget=widgets.PasswordInput)
    def save(self, user):
        fa, created = FetionAccount.objects.get_or_create(user=user)
        fa.username = self.cleaned_data['username']
        fa.password = self.cleaned_data['password']
        fa.save()

class TaskForm(forms.Form):
    trigger_kind = forms.CharField(max_length=32, widget=widgets.HiddenInput)
    trigger_source = forms.CharField(max_length=32, label=u'信号来源', widget=forms.TextInput, required=False)
    trigger_tag = forms.CharField(max_length=140, label=u'信号过滤', widget=forms.TextInput, required=False)
    action_kind = forms.CharField(max_length=32, widget=widgets.HiddenInput)
    action_destination = forms.CharField(max_length=32, label=u'行动目标', widget=forms.TextInput, required=False)
    action_content = forms.CharField(max_length=600, label=u'行动内容', widget=forms.Textarea)
    description = forms.CharField(max_length=600, label=u'描述你的涟漪', widget=forms.Textarea(attrs={'rows':4}))
    public = forms.BooleanField(initial=False, label=u'是否公开', required=False)
    parent = forms.IntegerField(min_value=0, widget=widgets.HiddenInput, required=False)

    def save(self, user):
        d = self.cleaned_data
        trigger = Trigger(kind=d['trigger_kind'], source=d['trigger_source'], content=d['trigger_tag'])
        trigger.save()
        action = Action(kind=d['action_kind'], destination=d['action_destination'], content=d['action_content'])
        action.save()
        task = Task(user=user, description=d['description'], parent=d['parent'], trigger=trigger, action=action, public=d['public'])
        task.save()
        return task

class TaskEditForm(TaskForm):
    id = forms.IntegerField(min_value=0, widget=widgets.HiddenInput)
    def save(self, user):
        d = self.cleaned_data
        task = Task.objects.get(pk=d['id'])
        task.__dict__.update(description=d.get('description'), public=d.get('public'))
        task.save()
        trigger = Trigger.objects.get(pk=task.trigger.id)
        trigger.__dict__.update(source=d.get('trigger_source'), content=d.get('trigger_tag'))
        trigger.save()
        action = Action.objects.get(pk=task.action.id)
        action.__dict__.update(destination=d.get('action_destination'), content=d.get('action_content'))
        action.save()
        return task
