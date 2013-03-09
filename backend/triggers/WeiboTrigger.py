from helper import *
from lib.weibo import Weibo
from email.utils import *

def test(trigger_info, action_info, user_info):
	ret = []
	acc_info = fetchByUserId('app_weiboaccount', user_info['id'])
	for status in Weibo(acc_info['access_token']).friend_timeline()['statuses']:
		if mktime_tz(parsedate_tz(status['created_at'])) > trigger_info['updated_at'] and status['text'].find(trigger_info['content']) != -1 and status['user']['name'].find(trigger_info['source']) != -1:
			fmt = action_info['content'].replace('{{username}}', status['user']['name'])
			fmt = fmt.replace('{{content}}', status['text'])
			ret.append(fmt.replace('{{createdAt}}', status['created_at']))

	return ret
