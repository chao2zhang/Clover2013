from helper import *
from lib.sinablog import * 

def post(pending_info, action_info):
	try:
		user_info, acc_info = getInfo(pending_info['action_id'], 'app_sinablogaccount')
		title, content = split_content(pending_info['content'])

		postblog(title, content, acc_info['username'], acc_info['password'])

		return True
	except:
		print_exc()
		return False
