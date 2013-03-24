from client import Client

CLIENT_ID = '1151462392'
CLIENT_SECRET = '5a8e10eab579cdc5e308533df6794835' 
AUTH_URI = 'https://api.weibo.com/oauth2/authorize'
TOKEN_URI = 'https://api.weibo.com/oauth2/access_token'
REDIRECT_URI = 'http://127.0.0.1/bind/weibo/'

class WeiboClient(Client):
	def __init__(self, client_id = CLIENT_ID, client_secret = CLIENT_SECRET):
		super(WeiboClient, self).__init__(CLIENT_ID, CLIENT_SECRET, AUTH_URI, TOKEN_URI)
	
	def get_auth_uri(self, scope):
		return super(WeiboClient, self).get_auth_uri(REDIRECT_URI, scope)

if __name__ == '__main__':
	client = WeiboClient()
	print client.get_auth_uri('status_update')
