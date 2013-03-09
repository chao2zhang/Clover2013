from helper import *
from lib.weibo import Weibo

def post(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_weiboaccount')

		weibo = Weibo(acc_info['access_token'])
		
		weibo.update_status(status=pending_info['content'].encode('utf-8'))
	except:
		print 'post weibo failed'
		print '-' * 50
		print pending_info
		print '-' * 50
		print action_info
		print '-' * 50
		return False

	return True
