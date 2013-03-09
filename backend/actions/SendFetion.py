from helper import *
from PyWapFetion import Fetion

def send2me(pending_info, action_info):
	print 'send a fetion to me'

def send2others(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_fetionaccount')
		
		client = Fetion(acc_info['username'], acc_info['password'])
		client.send([action_info['destination']], pending_info['content'])
		client.logout()
		return True
	except:
		print_exc()
		return False

def send2me(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_fetionaccount')
		
		client = Fetion(acc_info['username'], acc_info['password'])
		client.send2self(pending_info['content'])
		client.logout()
		return True
	except:
		print_exc()
		return False
