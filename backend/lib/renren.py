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


class SupportedAPI:
	def __init__(self, apiName, requiredScope):
		self.apiName = apiName
		self.requiredScope = requiredScope

class RenrenConfig:
		APP_API_KEY = "b934cf4d6b08490587c883a297aa0f29"
		APP_SECRET_KEY = "a460be7eee9b4049b6c55fcd963d53f7"

		SUPPORTED_REQUESTS = {
				'setStatus': SupportedAPI('status.set', ['status_update']),
				'forward': SupportedAPI('status.forward', ['status_update']),
				'getFeed': SupportedAPI('feed.get', ['read_user_feed'])
				#'share': SupportedAPI('share.share', ['publish_share']),
				#'addCommentToStatus': SupportedAPI('status.addComment', ['read_user_status' ,'publish_comment']),
				#'addCommentToBlog': SupportedAPI('blog.addComment', ['publish_blog' ,'publish_comment'])
		}

		AUTHORIZATION_URI = "http://graph.renren.com/oauth/authorize"
		ACCESS_TOKEN_URI = "http://graph.renren.com/oauth/token"
		SESSION_KEY_URI = "http://graph.renren.com/renren_api/session_key"
		API_SERVER = "https://api.renren.com/restserver.do"
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
	def __init__(self, access_token = None, api_key = RenrenConfig.APP_API_KEY, secret_key = RenrenConfig.APP_SECRET_KEY):
		self.access_token = access_token
		self.api_key = api_key
		self.secret_key = secret_key
    
	def getAuthUri(self):
		args = {
			'client_id': self.api_key,
			'response_type': 'code',
			'redirect_uri': RenrenConfig.LOGIN_SUCCESS,
			'scope': ''
		}
		scope = set()
		for api in RenrenConfig.SUPPORTED_REQUESTS.viewvalues():
			scope = scope.union(api.requiredScope)
		args['scope'] = ' '.join(s for s in scope)
		log(args['scope'])
		return "%s?%s" % (RenrenConfig.AUTHORIZATION_URI, urllib.urlencode(args))

	def auth(self, code):
		args = {
			'client_id': self.api_key,
			'client_secret': self.secret_key,
			'code': code,
			'grant_type': 'authorization_code',
			'redirect_uri': RenrenConfig.LOGIN_SUCCESS,
		}
		response = urllib.urlopen("%s?%s" % (RenrenConfig.ACCESS_TOKEN_URI, urllib.urlencode(args))).read()
		self.access_token = parse_json(response)["access_token"]
		"""
		'''Obtain session key from the Resource Service.''' 
		session_key_request_args = {"oauth_token": access_token}
		response = urllib.urlopen("%s?%s" % (RenrenConfig.SESSION_KEY_URI, urllib.urlencode(session_key_request_args))).read()
		log(response)
		self.session_key = str(parse_json(response)["renren_token"]["session_key"])
		"""
	
	def request(self, reqName, params = {}):
		if reqName in RenrenConfig.SUPPORTED_REQUESTS.keys():
				api = RenrenConfig.SUPPORTED_REQUESTS[reqName]
				params['method'] = api.apiName
				params["api_key"] = self.api_key
				params["call_id"] = str(int(time.time() * 1000))
				params["format"] = "json"
				params["access_token"] = self.access_token
				params["v"] = '1.0'
				sig = self.hash_params(params);
				#params["sig"] = sig
				post_data = None if not params else urllib.urlencode(params)
				response = urllib.urlopen(RenrenConfig.API_SERVER, post_data).read()
				j = parse_json(response)
				if isinstance(j, dict) and 'error_code' in j.keys():
						raise RenrenError(j['error_code'], j['error_msg'])
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

	def getFeed(self):
		return self.request('getFeed', {'type': '10', 'count': '50'})
			
	def setStatus(self, content):
		ret = self.request('setStatus', {'status': content})['result']
		if str(ret) != '1': 
			raise RenrenError(ret, 'setStatus failed')

	def foward(self, content, forward_id, forward_owner):
		self.request('forward', {'status': content, 'forward_id': forward_id, 'forward_owner': forward_owner})

class RenrenError(Exception):
	def __init__(self, code, message):
		Exception.__init__(self, message)
		self.code = code
		self.message = message
		print message

def log(msg):
	pass

if __name__ == '__main__':
	pass
