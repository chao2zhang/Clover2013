import sys
sys.path.append('..')

from DbUtils import *
from traceback import print_exc

def getInfo(aid, acc_table):
	task_info = execute('select * from app_task where action_id=' + str(aid)).fetchone()
	task_info = dict(zip(APP_TASK, task_info))
	user_info = fetchById('auth_user', task_info['user_id'])
	acc_info = fetchByUserId(acc_table, user_info['id'])
	return (user_info, acc_info)
