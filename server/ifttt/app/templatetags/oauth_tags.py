from django import template

from oauth.weibo import *
from oauth.renren import *

register = template.Library()
@register.simple_tag(name='weibo_auth_uri')
def weibo_auth_uri():
    return Weibo.auth_uri()