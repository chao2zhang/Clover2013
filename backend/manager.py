from time import sleep
import If, Then

def start():
	rd = 0
	while True:
		rd += 1
		print 'round: %d' % rd
		If.run()
		print '---------------Then--------------'
		Then.run()
		sleep(20)
