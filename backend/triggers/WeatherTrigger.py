from helper import *
from lib.weather import *
from time import localtime, mktime

def test(cond, trigger_info, action_info, user_info):
	#refresh every 12 hour
	'''
	if mktime(localtime()) - trigger_info['updated_at'] < 12 * 3600:
		return []
	'''

	try:
		weather = weather_forcast(trigger_info['source'], trigger_info['source'], 'china')
		if eval(cond):
			fmt = action_info['content'].replace('{{weather}}', weather['text'])
			fmt = fmt.replace('{{temperature}}', weather['low'] + '~' + weather['high'])
			return [fmt.replace('{{createdAt}}', weather['date'])]
		return []
	except:
		print_exc()
		return []

def testTemperature(trigger_info, action_info, user_info):
	cond = "trigger_info['kind'] == 'weather-smaller' and eval(weather['low']) < eval(trigger_info['content']) or trigger_info['kind'] == 'weather-larger' and eval(weather['high']) > eval(trigger_info['content'])"
	return test(cond, trigger_info, action_info, user_info)

def testRain(trigger_info, action_info, user_info):
	cond = "weather['text'].lower().find('rain') != -1"
	return test(cond, trigger_info, action_info, user_info)
