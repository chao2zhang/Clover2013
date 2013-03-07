from helper import *
from lib.renren import RenrenClient

def test(action_info, trigger_info, user_info):
	print trigger_info
	print '*' * 50
	print user_info
	print '*' * 50
	ret = []
	acc_info = fetchByUserId('app_renrenaccount', user_info['id'])
	print acc_info
	last_updated = str2time(trigger_info['updated_at'])

	feed = RenrenClient(acc_info['access_token']).getFeed()
	for status in feed:
		if str2time(status['update_time']) > last_updated and status['name'].find(trigger_info['source']) != -1 and status['message'].find(trigger_info['content']) != -1:
			fmt = action_info['content'].replace('{{username}}', status['name'])
			fmt = fmt.replace('{{content}}', status['message'])
			print fmt
			ret.append(fmt.replace('{{createdAt}}', status['update_time']))

	return ret 
