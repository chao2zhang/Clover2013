from helper import *
import lib.mail, sqlite3

def test(trigger_info, user_info):
	print trigger_info
	print user_info
	con = sqlite3.connect('sqlite.db')

