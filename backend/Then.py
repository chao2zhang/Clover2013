import sqlite3
from DbUtils import *

from actions import *
'''
HANDLER(pending_info, action_info)
return true if success
'''
HANDLERS = { 
	'fudan-send2me': SendFudanMail.send2me,
	'fudan-send2others': SendFudanMail.send2others,
	'renren-post': PostRenren.post,
	'weibo-post': PostWeibo.post
	} 

def run():
	for pending in execute('select * from app_pending'):
		pending_info = dict(zip(APP_PENDING, pending))	
		action_info = fetchById('app_action', pending_info['action_id'])	

		if HANDLERS[action_info['kind']](pending_info, action_info):
			execute('delete from app_pending where id=' + pending_info['id'])
	con.commit()

if __name__ == '__main__':
	pass
