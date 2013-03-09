from helper import *

def send2me(pending_info, action_info):
	print 'send a fetion to me'

def send2others(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_fetionaccount')

		print 'send a fetion to some one'
		return True
	except:
		print_exc()
		return False

