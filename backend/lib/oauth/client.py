import json
from urllib2 import urlopen
from urllib import urlencode

class Client(object):
	def __init__(self, client_id, client_secret, auth_uri, token_uri):
		self.client_id = client_id
		self.client_secret = client_secret
		self.auth_uri = auth_uri
		self.token_uri = token_uri

	def get_auth_uri(self, redirect_uri, scope):
		params = {
			'client_id': self.client_id,
			'response_type': 'code',
			'redirect_uri': redirect_uri,
			'scope': scope
		}
		return '%s?%s' % (self.auth_uri, urlencode(params))
	
	def auth(self, redirect_uri, code):
		params = {
			'client_id': self.client_id,
			'client_secret'	: self.client_secret,
			'code': code,
			'redirect_uri': redirect_uri,
			'grant_type': 'authorization_code',
		}
		response = urlopen(self.token_uri, urlencode(params)).read()
		try:
			data = json.loads(response)
		except:
			data = {}
			for attr in response.split('&'):
				tmp = attr.split('=')
				data[tmp[0]] = tmp[1]
		self.required_params = {
			'access_token': data['access_token']}

	def post(self, uri, params):
		params.update(self.required_params)
		response = urlopen(uri, urlencode(params)).read()
		return json.loads(response)		
	
	def get(self, uri, params):
		params.update(self.required_params)
		response = urlopen('%s?%s' % (uri, urlencode(params))).read()
		return json.loads(response)
