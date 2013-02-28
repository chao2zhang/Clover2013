from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from models import WeiboAccount

def dashboard(request):
    t = 'dashboard/dashboard.html'
    return render_to_response(t, context_instance=RequestContext(request))

def bind(request):
    t = 'dashboard/bind.html'
    return render_to_response(t, context_instance=RequestContext(request))

@require_GET
@login_required
def bind_weibo(request):
    if request.GET.get('code'):
        request.flash['message'] = 'Weibo binded successfully'
        wa, created = WeiboAccount.objects.get_or_create(user=request.user)
        wa.access_token = request.GET['code']
        wa.save()
    else:
        request.flash['message'] = 'Canceled'
    return redirect(bind)