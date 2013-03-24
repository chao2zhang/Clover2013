from client import Client

CLIENT_ID = '801327084'
CLIENT_SECRET = 'd716ef7ae982cc874c01b351a153ce33'
AUTH_URI = 'https://open.t.qq.com/cgi-bin/oauth2/authorize'
TOKEN_URI = 'https://open.t.qq.com/cgi-bin/oauth2/access_token'
REDIRECT_URI = 'http://127.0.0.1'

class TencentClient(Client):
	def __init__(self, client_id = CLIENT_ID, client_secret = CLIENT_SECRET):
		super(TencentClient, self).__init__(CLIENT_ID, CLIENT_SECRET, AUTH_URI, TOKEN_URI)
	
	def auth(self, redirect_uri, code, openid):
		super(TencentClient, self).auth(redirect_uri, code)
		self.required_params.update({
			'oauth_consumer_key': CLIENT_ID,
			'openid': openid,
			'oauth_version': '2.a',
			'format': 'json',
			'scope': 'all'
		})

if __name__ == '__main__':
	client = TencentClient()
	print client.get_auth_uri('http://127.0.0.1', 'all')
