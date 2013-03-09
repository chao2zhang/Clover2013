from helper import *
from lib.weibo import Weibo

def post(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_weiboaccount')

		weibo = Weibo(acc_info['access_token'])
		weibo.update_status(status=pending_info['content'].replace('\n', ' ').replace('\r', ' ').encode('utf-8'))
	except:
		print_exc()
		return False
	return True
