from helper import *
from lib.sinablog import * 

def post(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_sinablogaccount')

		print 'post a sina blog'

		return True
	except:
		print_exc()
		return False
