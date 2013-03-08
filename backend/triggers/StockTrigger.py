from helper import *
from lib.stock import *

def test(trigger_info, action_info, user_info):
	cond = eval(trigger_info['content'])
	id_ = eval(trigger_info['source'])
	price = stock(id_)
	if trigger_info['kind'] == 'stock-larger' and price > cond or trigger_info['kind'] == 'stock-smaller' and price < cond:
		return [action_info['content'].replace('{{id}}', str(id_)).replace('{{name}}', str(id_)).replace('{{price}}', str(price))]
