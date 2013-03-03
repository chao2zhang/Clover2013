from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^server/', include('server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
    url(r'^accounts/register/$', 'registration.views.register', name='register'),
    url(r'^$', 'registration.views.home', name='home'),

    url(r'^dashboard/$', 'app.views.dashboard', name='dashboard'),
    url(r'^bind/$', 'app.views.bind', name='bind'),
    url(r'^bind/weibo/$', 'app.views.bind_weibo', name='bind_weibo'),
    url(r'^bind/renren/$', 'app.views.bind_renren', name='bind_renren'),
    url(r'^bind/fudan/$', 'app.views.bind_fudan', name='bind_fudan'),
    url(r'^bind/fetion/$', 'app.views.bind_fetion', name='bind_fetion'),
    url(r'^tasks/new/$', 'app.views.new_task', name="new_task"),
    url(r'^tasks/(?P<id>\d+)/$', 'app.views.show_task', name="show_task"),
    url(r'^tasks/(?P<id>\d+)/edit/$', 'app.views.edit_task', name="edit_task"),
    url(r'^tasks/(?P<id>\d+)/clone/$', 'app.views.clone_task', name="clone_task"),
    url(r'^tasks/(?P<id>\d+)/delete/$', 'app.views.delete_task', name="delete_task"),
    url(r'^tasks/list_hot/$', 'app.views.list_hot', name="list_hot"),
    url(r'^user/(?P<id>\d+)/$', 'app.views.list', name="list_task"),
)
