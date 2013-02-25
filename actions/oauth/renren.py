#!/usr/bin/env python
#coding=utf-8
# 
# Copyright 2010 RenRen
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


class RenrenConfig:
    APP_API_KEY = "b934cf4d6b08490587c883a297aa0f29"
    APP_SECRET_KEY = "a460be7eee9b4049b6c55fcd963d53f7"

    AUTHORIZATION_URI = "http://graph.renren.com/oauth/authorize"
    ACCESS_TOKEN_URI = "http://graph.renren.com/oauth/token"
    SESSION_KEY_URI = "http://graph.renren.com/renren_api/session_key"
    API_SERVER = "http://api.renren.com/restserver.do"
    LOGIN_SUCCESS = "http://graph.renren.com/oauth/login_success.html"
    

import hashlib
import time
import urllib

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

class RenrenClient(object):
    def __init__(self, session_key = None, api_key = RenrenConfig.APP_API_KEY, secret_key = RenrenConfig.APP_SECRET_KEY):
        self.session_key = session_key
        self.api_key = api_key
        self.secret_key = secret_key
    
    def auth(self):
        args = {
            'client_id': self.api_key,
            'response_type': 'code',
            'redirect_uri': RenrenConfig.LOGIN_SUCCESS,
            'scope': 'status_update',
        }
        url = "%s?%s" % (RenrenConfig.AUTHORIZATION_URI, urllib.urlencode(args))
        print 'Please authorize: ' + url
        verification_code = raw_input('PIN:')
        args = {
            'client_id': self.api_key,
            'client_secret': self.secret_key,
            'code': verification_code,
            'grant_type': 'authorization_code',
            'redirect_uri': RenrenConfig.LOGIN_SUCCESS,
        }
        response = urllib.urlopen("%s?%s" % (RenrenConfig.ACCESS_TOKEN_URI, urllib.urlencode(args))).read()
        print response
        access_token = parse_json(response)["access_token"]
        '''Obtain session key from the Resource Service.'''
        session_key_request_args = {"oauth_token": access_token}
        response = urllib.urlopen("%s?%s" % (RenrenConfig.SESSION_KEY_URI, urllib.urlencode(session_key_request_args))).read()
        print response
        self.session_key = str(parse_json(response)["renren_token"]["session_key"])

    def request(self, params = {}}):
        """
        Fetches the given method's response returning from RenRen API.
        Send a POST request to the given method with the given params.
        """
        params["api_key"] = self.api_key
        params["call_id"] = str(int(time.time() * 1000))
        params["format"] = "json"
        params["session_key"] = self.session_key
        params["v"] = '1.0'
        sig = self.hash_params(params);
        params["sig"] = sig
        post_data = None if not params else urllib.urlencode(params)
        response = urllib.urlopen(RenrenConfig.API_SERVER, post_data).read()
        j = parse_json(response)
        return j
    def hash_params(self, params = None):
        hasher = hashlib.md5("".join(["%s=%s" % (self.unicode_encode(x), self.unicode_encode(params[x])) for x in sorted(params.keys())]))
        hasher.update(self.secret_key)
        return hasher.hexdigest()
    def unicode_encode(self, str):
        """
        Detect if a string is unicode and encode as utf-8 if necessary
        """
        return isinstance(str, unicode) and str.encode('utf-8') or str

class RenrenError(Exception):
    def __init__(self, code, message):
        Exception.__init__(self, message)
        self.code = code
        self.message = message