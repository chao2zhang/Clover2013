from time import sleep
import If, Then

SHORT = ['fudan-new', 'weibo-new', 'renren-new', 'wangyi-new', 'stock-larger', 'stock-smaller']
LONG = ['weather-larger', 'weather-smaller', 'weather-rain']

def start():
	rd = 0
	while True:
		rd += 1
		print 'round: %d' % rd
		If.run(SHORT)
		if rd % 3 == 0:
			If.run(LONG)
		print '---------------Then--------------'
		Then.run()
		sleep(20)
