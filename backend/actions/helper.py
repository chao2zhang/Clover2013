import sys
sys.path.append('..')

from DbUtils import *

def getInfo(uid, acc_table):
	user_info = fetchById('auth_user', uid)
	acc_info = fetchByUserId(acc_table, user_info['id'])
	return (user_info, acc_info)
