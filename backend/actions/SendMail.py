from helper import *
from lib.mail import SmtpClient

def send2others(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_fudanaccount')

		smtp = SmtpClient(acc_info['username'], acc_info['password'])	
		smtp.send(acc_info['username'], [action_info['destination']], 'hello from ripple', pending_info['content'])
	except:
		print 'send mail failed'
		print pending_info
		print '-' * 50
		print action_info
		print '-' * 50
		return False
	
	return True

SMTP_ACC = 'RippleServer@163.com'
ACC_PWD = 'chaomataiqiangle'

def send2me(pending_info, action_info):
	'''
	send an email to user from his own email account-_-
	'''
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_fudanaccount')

		smtp = SmtpClient(SMTP_ACC, ACC_PWD, 'smtp.163.com')
		smtp.send(SMTP_ACC, [user_info['email']], 'hello from ripple', pending_info['content'])
	except:
		print 'send mail failed'
		print pending_info
		print '-' * 50
		print action_info
		print '-' * 50
		return False
	
	return True
