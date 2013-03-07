from helper import *
from lib.weibo import Weibo

def post(pending_info, action_info):
	print pending_info
	print '-' * 50
	print action_info
	print '-' * 50
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_weiboaccount')

		weibo = Weibo(acc_info['access_token'])

	except:
		return False
	return True
