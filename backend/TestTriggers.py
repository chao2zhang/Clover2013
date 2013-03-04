import sqlite3
from DbConfig import *

import FudanMailTrigger, WeiboTrigger, RenrenTrigger
HANDLERS = {'mail-new': FudanMailTrigger.test, 'weibo-new': WeiboTrigger.test, 'renren-new': RenrenTrigger.test}

def run():
	con = sqlite3.connect(DB_NAME)
	for task in con.cursor().execute('select * from app_task'):
		task_info = dict(zip(APP_TASK, task))
		user_info = dict(zip(AUTH_USER, con.cursor('select * from auth_user where id=%s' % task_info['user_id'])))
		trigger_info = dict(zip(APP_TRIGGER, con.cursor('select * from app_trigger where id=%s' % task_info['trigger_id'])))
		action_info = dict(zip(APP_ACTION, con.cursor('select * from app_action where id=%s' % task_info['action_id'])))

		pending_info = HANDLERS[trigger_info['kind']](trigger_info, user_info)
		con.cursor().execute("update %s set updated_at = datetime('now') where id = %s" % (TABLE_NAME, info['id']))
	con.commit()	
	con.close()

if __name__ == '__main__':
	pass
