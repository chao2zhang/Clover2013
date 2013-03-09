from helper import *
from lib.renren import RenrenClient

def post(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_renrenaccount')

		renren = RenrenClient(acc_info['access_token'])
		renren.setStatus(pending_info['content'].encode('utf-8'))

	except:
		print 'post renren failed'
		print '-' * 50
		print pending_info
		print '-' * 50
		print action_info
		print '-' * 50
		return False
	return True
