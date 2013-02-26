#!/usr/bin/env python
#coding=utf-8
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


class WeiboConfig:
    APP_API_KEY = "1151462392"
    APP_SECRET_KEY = "5a8e10eab579cdc5e308533df6794835"

    AUTHORIZATION_URI = "https://api.weibo.com/oauth2/authorize"
    ACCESS_TOKEN_URI = "https://api.weibo.com/oauth2/access_token"
    LOGIN_SUCCESS = "http://graph.renren.com/oauth/login_success.html"
    

import hashlib
import time
import urllib, urllib2

# Find a JSON parser
try:
    import json
    parse_json = lambda s: json.loads(s)
except ImportError:
    try:
        import simplejson
        parse_json = lambda s: simplejson.loads(s)
    except ImportError:
        # For Google AppEngine
        from django.utils import simplejson
        parse_json = lambda s: simplejson.loads(s)

class Weibo(object):
    def __init__(self, api_key = WeiboConfig.APP_API_KEY, secret_key = WeiboConfig.APP_SECRET_KEY, access_token = '805ebefa6fcce01846927e945c49c922'):
        self.api_key = api_key
        self.secret_key = secret_key
        self.access_token = access_token
    
    def auth(self):
        args = {
            'client_id': self.api_key,
            'response_type': 'code',
            'redirect_uri': WeiboConfig.LOGIN_SUCCESS,
            'scope': 'status_update',
        }
        url = "%s?%s" % (WeiboConfig.AUTHORIZATION_URI, urllib.urlencode(args))
        print 'Please authorize: ' + url
        verification_code = raw_input('PIN:')
        args = {
            'client_id': self.api_key,
            'client_secret': self.secret_key,
            'code': verification_code,
            'grant_type': 'authorization_code',
            'redirect_uri': WeiboConfig.LOGIN_SUCCESS,
        }
        response = urllib2.urlopen(WeiboConfig.ACCESS_TOKEN_URI, urllib.urlencode(args)).read()
        print response
        self.access_token = parse_json(response)["access_token"]
        return self.access_token

    def post(self, uri, params = {}):
        """
        Fetches the given method's response returning from Weibo API.
        Send a POST request to the given method with the given params.
        """
        params["access_token"] = self.access_token
        params = urllib.urlencode(params)
        response = urllib2.urlopen(uri, params).read()
        j = parse_json(response)
        return j

    def get(self, uri, params = {}):
        params["access_token"] = self.access_token
        params = urllib.urlencode(params)
        response = urllib2.urlopen('%s?%s' % (uri, params)).read() 
        j = parse_json(response)
        return j

    def update_status(self, **kwargs):
        return self.post('https://api.weibo.com/2/statuses/update.json', kwargs)

    def friend_timeline(self, **kwargs):
        if kwargs:
            return self.get('https://api.weibo.com/2/statuses/friends_timeline.json', kwargs)
        else:
            return self.get('https://api.weibo.com/2/statuses/friends_timeline.json')

    def trigger(self, created_at=None, user=None, tag=None):
        l = self.friend_timeline().get('statuses')
        if not l: return 0
        i = 0
        while created_at and l[:-1]['created_at'] > created_at:
            i += 1
            ll = self.friend_timeline({'page': i}).get('statuses')
            if ll: break
            l.append(ll)
        if user:
            l = filter(lambda x: x['user']['name'] == user or x['user']['screen_name'] == user, l)
        if tag:
            l = filter(lambda x: x['text'].find(tag) > -1, l)
        return len(l)

