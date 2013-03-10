# DB_NAME = '/home/xc/Desktop/Clover2013/server/ripple/sqlite.db'
DB_NAME = '/Users/chaozhang/Development/clover/server/ripple/sqlite.db'

APP_TRIGGER = ('id', 'kind', 'source', 'content', 'updated_at')
APP_TASK = ('id', 'user_id', 'trigger_id', 'action_id', 'parent_id', 'description', 'created_at', 'count', 'public')
APP_PENDING = ('id', 'action_id', 'done', 'content')
APP_ACTION = ('id', 'kind', 'destination', 'content')
AUTH_USER = ('id', 'user_name', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
APP_FUDANACCOUNT = ('id', 'username', 'password', 'user_id')
APP_RENRENACCOUNT = ('id', 'access_token', 'user_id')
APP_WEIBOACCOUNT = ('id', 'access_token', 'user_id')
APP_FETIONACCOUNT = ('id', 'username', 'password', 'user_id')
APP_WANGYIACCOUNT = ('id', 'username', 'password', 'user_id')
APP_SINABLOGACCOUNT = ('id', 'username', 'password', 'user_id')

import sqlite3
from time import strptime, mktime


def execute(sql):
	con = sqlite3.connect(DB_NAME)
	ret = con.cursor().execute(sql).fetchall()
	con.commit()
	con.close()
	return ret

def fetchById(table, id_):
	data = execute('select * from %s where id=%s' % (table, id_))[0]
	return dict(zip(eval(table.upper()), data))

def fetchByUserId(table, id_):
	return dict(zip(eval(table.upper()), execute('select * from %s where user_id=%s' % (table, id_))[0]))

def insert(table, info):
	columns = ','.join(str(item[0]) for item in info.items())
	values = ','.join("'" + item[1] + "'"  if isinstance(item[1], str) or isinstance(item[1], unicode) else str(item[1]) for item in info.items())
	sql = "insert into %s (%s) values (%s)" % (table, columns, values)
	execute(sql)

def str2time(str_):
	return mktime(strptime(str_.partition('.')[0], '%Y-%m-%d %H:%M:%S'))

def clearPending():
	execute('delete from app_pending where done=0')

if __name__ == '__main__':
	test = {'action_id': 1, 'user_id': 1, 'content': 'hello'}
