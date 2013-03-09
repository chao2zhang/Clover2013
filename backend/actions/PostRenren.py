from helper import *
from lib.renren import RenrenClient

def post(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_renrenaccount')

		renren = RenrenClient(acc_info['access_token'])
		renren.setStatus(pending_info['content'].replace('\n', ' ').encode('utf-8'))

		return True
	except:
		print_exc()
		return False
