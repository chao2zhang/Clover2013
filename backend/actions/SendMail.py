from helper import *
from lib.mail import SmtpClient

ACCOUNT_TABLE = {
	"smtp.163.com": "app_wangyiaccount",
	"mail.fudan.edu.cn": "app_fudanaccount"
}

def send2others(host, pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], ACCOUNT_TABLE['host'])
		title, content = split_content(pending_info['content']

		smtp = SmtpClient(acc_info['username'], acc_info['password'], host)

		smtp.send(acc_info['username'], [action_info['destination']], title, content)
		return True
	except:
		print_exc()
		return False
	

def sendfudan(pending_info, action_info):
	return send2others('mail.fudan.edu.cn', pending_info, action_info)

def send163(pending_info, action_info):
	return send2others('smtp.163.com', pending_info, action_info)

SMTP_ACC = 'RippleServer@163.com'
ACC_PWD = 'chaomataiqiangle'

def send2me(pending_info, action_info):
	'''
	send an email to user from our account
	'''
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_fudanaccount')
		title, content = split_content(pending_info['content']

		smtp = SmtpClient(SMTP_ACC, ACC_PWD, 'smtp.163.com')
		smtp.send(SMTP_ACC, [user_info['email']], 'hello from ripple', pending_info['content'])
		return True
	except:
		print_exc()
		return False
	
