from helper import *
from lib.sinablog import *

def post(pending_info, action_info):
	user_info, acc_info = getInfo(pending_info['action_id'], 'app_weiboaccount')

	print 'post a sina blog'