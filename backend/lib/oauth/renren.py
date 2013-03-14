from client import Client

CLIENT_ID = 'b934cf4d6b08490587c883a297aa0f29'
CLIENT_SECRET = 'a460be7eee9b4049b6c55fcd963d53f7'
AUTH_URI = 'http://graph.renren.com/oauth/authorize'
TOKEN_URI = 'http://graph.renren.com/oauth/token'
POST_URI = 'https://api.renren.com/restserver.do'

class RenrenClient(Client):

	def __init__(self, client_id = CLIENT_ID, client_secret = CLIENT_SECRET):
		super(RenrenClient, self).__init__(client_id, client_secret, AUTH_URI, TOKEN_URI)
	
	def auth(self, redirect_uri, code):
		super(RenrenClient, self).auth(redirect_uri, code)
		self.required_params.update({
			'api_key': CLIENT_ID,
			'format': 'json',
			'v': '1.0'
		})
	
	def post(self, params):
		return super(RenrenClient, self).post(POST_URI, params)

if __name__ == '__main__':
	client = RenrenClient()
	print client.get_auth_uri('http://127.0.0.1', 'read_user_feed status_update')
