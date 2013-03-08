from helper import *
from lib.mail import PopClient
from time import ctime

def test(pop_host, trigger_info, action_info, user_info):
	acc_info = fetchByUserId('app_fudanaccount', user_info['id'])
	last_updated = str2time(trigger_info['updated_at'])
	pop = PopClient(acc_info['username'], acc_info['password'], pop_host)
	ret = []
	for i in range(pop.count()):
		msg = pop.fetch(i + 1)
		if msg['Date'] > last_updated and msg['Subject'].find(trigger_info['content']) != -1:
			for item in msg['From']:
				if item.find(trigger_info['source']) != -1:
					fmt = action_info['content'].replace('{{username}}', ''.join(msg['From']))
					fmt = fmt.replace('{{title}}', msg['Subject'])
					ret.append(fmt.replace('{{createdAt}}', ctime(msg['Date'])))
					break
	return ret

def testFudan(trigger_info, action_info, user_info):
	return test('mail.fudan.edu.cn', trigger_info, action_info, user_info)

def test163(trigger_info, action_info, user_info):
	return test('pop3.163.com', trigger_info, action_info, user_info)
