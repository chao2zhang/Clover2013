import sqlite3
from DbUtils import *

from triggers import *
'''
HANDLER(trigger_info, action_info, user_info)
return list of content should be logged into table app_pending
each item in the list generate a app_pending entry 
return [] when fail
'''
HANDLERS = {
	'fudan-new': MailTrigger.testFudan, 
	'weibo-new': WeiboTrigger.test, 
	'renren-new': RenrenTrigger.test,
	'wangyi-new': MailTrigger.test163,
	'weather-larger': WeatherTrigger.testTemperature,
	'weather-smaller': WeatherTrigger.testTemperature,
	'weather-rain': WeatherTrigger.testRain,
	'stock-larger': StockTrigger.test,
	'stock-smaller': StockTrigger.test
	}

def log(msg):
	print msg

def run():
	for task in execute('select * from app_task'):
		task_info = dict(zip(APP_TASK, task))
		user_info = fetchById('auth_user', task_info['user_id']) 
		trigger_info = fetchById('app_trigger', task_info['trigger_id'])
		action_info = fetchById('app_action', task_info['action_id'])

		trigger_info['updated_at'] = str2time(trigger_info['updated_at']) + 8 * 3600

		log(trigger_info['kind'])

		pending_info = {'done': 0, 'action_id': task_info['action_id']}
		content = HANDLERS[trigger_info['kind']](trigger_info, action_info, user_info)
		
		for c in content:
			pending_info['content'] = c
			log(pending_info)
			insert('app_pending', pending_info)
		execute("update app_trigger set updated_at = datetime('now') where id = %s" % trigger_info['id'])

if __name__ == '__main__':
	pass
