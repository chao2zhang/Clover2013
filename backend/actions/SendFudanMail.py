from helper import *
from lib.mail import SmtpClient

def send2others(pending_info, action_info):
	print pending_info
	print '-' * 50
	print action_info
	print '-' * 50
	try:
		user_info, acc_info = getInfo(pending_info['user_id'], 'app_fudanaccount')

		smtp = SmtpClient(acc_info['username'], acc_info['password'])	
		smtp.send(acc_info['username'], [action_info['destination']], 'hello from ripple', pending_info['content'])
	except:
		return False
	
	return True

def send2me(pending_info, action_info):
	'''
	send an email to user from his own email account-_-
	'''
	print pending_info
	print '-' * 50
	print action_info
	print '-' * 50
	try:
		user_info, acc_info = getInfo(pending_info['user_id'], 'app_fudanaccount')

		smtp = SmtpClient(acc_info['username'], acc_info['password'])	
		smtp.send('ripple', [user_info['email']], 'hello from ripple', pending_info['content'])
	except:
		return False
	
	return True
