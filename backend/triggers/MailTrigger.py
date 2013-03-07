from helper import *
from lib.mail import PopClient

def testFudan(trigger_info, user_info):
	print trigger_info
	print '*' * 50
	print user_info
	print '*' * 50
	acc_info = fetchByUserId('app_fudanaccount', user_info['id'])
	try:
		pop = PopClient(acc_info['username'], acc_info['password'])
		ret = []
		for i in range(pop.count()):
			msg = pop.fetch(i + 1)
			if msg['Date'] > str2time(trigger_info['updated_at']) and msg['Subject'].find(trigger_info['content']) != -1:
				for item in msg['From']:
					if item.find(trigger_info['source']) != -1:
						ret.append(msg['Subject'])
						break
		return ret
	except:
		return []
