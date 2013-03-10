from helper import *
from PyWapFetion import send, send2self

def send2others(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_fetionaccount')
		
		send(acc_info['username'], acc_info['password'], action_info['destination'], pending_info['content'].encode('utf-8'))
		return True
	except:
		print_exc()
		return False

def send2me(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_fetionaccount')

		send2self(acc_info['username'], acc_info['password'], pending_info['content'].encode('utf-8'))
		return True
	except:
		print_exc()
		return False
