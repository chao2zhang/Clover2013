from helper import *
from lib.weather import *
from time import localtime, mktime

def test(trigger_info, action_trigger, user_info):
	last_updated = str2time(trigger_info['updated_at'])
	#refresh every 12 hour
	if mktime(localtime()) - last_updated < 12 * 3600:
		return []

	cond = eval(trigger_info['content'])
	weather = weather_forcast(trigger_info['source'], trigger_info['source'], 'china')
	if trigger_info['kind'] == 'weather-smaller' and eval(weather['low']) < cond or trigger_info['kind'] == 'weather-larger' and eval(weather['high']) > cond:
		fmt = action_trigger['content'].replace('{{weather}}', weather['text'])
		fmt = fmt.replace('{{temperature}}', weather['low'] + '~' + weather['high'])
		return [fmt.replace('{{createdAt}}', weather['date'])]

