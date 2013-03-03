from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.views import login
from forms import UserCreationForm

def register(request):
    t = 'registration/register.html'
    #if request.user.is_authenticated():
    #    return render_to_response(t)
    form = UserCreationForm()
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.flash['alert-success'] = 'Account created successfully'
            return redirect(login)
    return render_to_response(t, {'form': form}, context_instance=RequestContext(request))

def home(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    t = 'registration/home.html'
    return render_to_response(t, context_instance=RequestContext(request))