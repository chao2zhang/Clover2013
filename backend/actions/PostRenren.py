from helper import *
from lib.renren import RenrenClient

def post(pending_info, action_info):
	print pending_info
	print '-' * 50
	print action_info
	print '-' * 50
	try:
		user_info, acc_info = getInfo(pending_info['user_info'], 'app_renrenaccount')

		renren = RenrenClient(acc_info['access_token'])
		renren.setStatus(pending_info['content'])

	except:
		return False
	return True
