# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.contrib.auth.models import User
from models import *
from forms import TaskForm, TaskEditForm, FudanAccountForm, FetionAccountForm

@login_required
def dashboard(request):
    t = 'dashboard/dashboard.html'
    b = binds(request.user)
    tasks = request.user.tasks.all()
    return render_to_response(t, {
        'binds': b,
        'tasks': tasks,
        }, context_instance=RequestContext(request))

@login_required
def bind(request):
    t = 'dashboard/bind.html'
    b = binds(request.user)
    return render_to_response(t, {
        'binds': b,
        }, context_instance=RequestContext(request))

@login_required
def new_task(request):
    t = 'dashboard/new_task.html'
    form = TaskForm()
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(request.user)
            request.flash['alert-success'] = u'涟漪创建成功'
            return redirect(task)

    print form.errors
    return render_to_response(t, {
        'triggers'  :active_triggers(request.user),
        'actions'   :active_actions(request.user),
        'form'      :form
        }, context_instance=RequestContext(request))

@require_GET
@login_required
def show_task(request, id):
    t = 'dashboard/show_task.html'
    task = get_object_or_404(Task, pk=id)
    return render_to_response(t, {
        'task': task,
        }, context_instance=RequestContext(request))

@login_required
def edit_task(request, id):
    t = 'dashboard/edit_task.html'
    task = get_object_or_404(Task, pk=id, user=request.user)
    d = {
        'trigger_kind'      :task.trigger.kind,
        'trigger_source'    :task.trigger.source,
        'trigger_content'   :task.trigger.content,
        'action_kind'       :task.action.kind,
        'action_source'     :task.action.source,
        'action_destination':task.action.destination,
        'action_content'    :task.action.content,
        'description'       :task.description,
        'parent'            :task.parent.id if task.parent else None,
        'id'                :task.id,
        'public'            :task.public,
    }
    form = TaskEditForm(initial=d)
    if request.POST:
        form = TaskEditForm(request.POST)
        if form.is_valid():
            task = form.save(request.user)
            request.flash['alert-success'] = u'涟漪编辑成功'
            return redirect(task)
    return render_to_response(t, {
        'form': form,
        'task': task,
        }, context_instance=RequestContext(request))

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    task.delete()
    return redirect(dashboard)

@login_required
def clone_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task = task.clone(request.user)
    request.flash['alert-success'] = u'涟漪复制成功'
    return redirect(edit_task, id=task.id)

@login_required
def list(request, id):
    t = 'dashboard/list.html'
    user = get_object_or_404(User, pk=id)
    tasks = user.tasks.all()
    return render_to_response(t, {
        'tasks': tasks,
        }, context_instance=RequestContext(request))

@login_required
def list_hot(request):
    t = 'dashboard/list_hot.html'
    tasks = Task.objects.filter(public=True).order_by('-count')[:100]
    return render_to_response(t, {
        'tasks': tasks,
        }, context_instance=RequestContext(request))

@require_GET
@login_required
def bind_weibo(request):
    if request.GET.get('code'):
        request.flash['alert-success'] = 'Weibo binded successfully'
        wa, created = WeiboAccount.objects.get_or_create(user=request.user)
        wa.access_token = request.GET['code']
        wa.save()
    else:
        request.flash['alert-error'] = u'已取消授权'
    return redirect(bind)

@require_GET
@login_required
def bind_renren(request):
    if request.GET.get('code'):
        request.flash['alert-success'] = u'人人绑定成功'
        ra, created = RenrenAccount.objects.get_or_create(user=request.user)
        ra.access_token = request.GET['code']
        ra.save()
    else:
        request.flash['alert-error'] = '已取消授权'
    return redirect(bind)

@login_required
def bind_fetion(request):
    t = 'dashboard/bind_fetion.html'
    form = FetionAccountForm()
    if request.POST:
        form = FetionAccountForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            request.flash['alert-success'] = u'飞信绑定成功'
            return redirect(bind)
    return render_to_response(t, {
        'form':form,
        }, context_instance=RequestContext(request))

@login_required
def bind_fudan(request):
    t = 'dashboard/bind_fudan.html'
    form = FudanAccountForm()
    if request.POST:
        form = FudanAccountForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            request.flash['alert-success'] = u'复旦邮箱绑定成功'
            return redirect(bind)
    return render_to_response(t, {
        'form':form,
        }, context_instance=RequestContext(request))