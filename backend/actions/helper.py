import sys
sys.path.append('..')

from DbUtils import *

def getInfo(uid, acc_table):
	user_info = fetchById('auth_user', uid)
	acc_info = dict(zip(acc_table.upper(), execute('select * from %s where user_id=%s' % (acc_table, user_info['id'])).fetchone()))
	return (user_info, acc_info)
