from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ifttt.views.home', name='home'),
    # url(r'^ifttt/', include('ifttt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/register/$', 'registration.views.register', name='register'),
    url(r'^$', 'registration.views.home', name='home'),

    url(r'^dashboard/$', 'app.views.dashboard', name='dashboard'),
    url(r'^bind/$', 'app.views.bind', name='bind'),
    url(r'^bind/weibo/$', 'app.views.bind_weibo', name='bind_weibo'),
)
