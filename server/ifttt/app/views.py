from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from models import WeiboAccount, RenrenAccount, FetionAccount, FudanAccount
from trigger import active_triggers
from action import active_actions
from forms import TaskForm, FudanAccountForm, FetionAccountForm

@login_required
def dashboard(request):
    t = 'dashboard/dashboard.html'
    return render_to_response(t, context_instance=RequestContext(request))

@login_required
def bind(request):
    t = 'dashboard/bind.html'
    return render_to_response(t, context_instance=RequestContext(request))

@login_required
def new_task(request):
    t = 'dashboard/new_task.html'
    form = TaskForm()
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            request.flash['alert-success'] = 'Task created successfully'
            return redirect(dashboard)

    return render_to_response(t, {
        'triggers'  :active_triggers(request.user),
        'actions'   :active_actions(request.user),
        'form'      :form
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
        request.flash['alert-error'] = 'Canceled'
    return redirect(bind)

@require_GET
@login_required
def bind_renren(request):
    if request.GET.get('code'):
        request.flash['alert-success'] = 'Renren binded successfully'
        ra, created = RenrenAccount.objects.get_or_create(user=request.user)
        ra.access_token = request.GET['code']
        ra.save()
    else:
        request.flash['alert-error'] = 'Canceled'
    return redirect(bind)

@login_required
def bind_fetion(request):
    t = 'dashboard/bind_fetion.html'
    form = FetionAccountForm()
    if request.POST:
        form = FetionAccountForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            request.flash['alert-success'] = 'Fetion binded successfully'
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
            request.flash['alert-success'] = 'FudanMail binded successfully'
            return redirect(bind)
    return render_to_response(t, {
        'form':form,
        }, context_instance=RequestContext(request))