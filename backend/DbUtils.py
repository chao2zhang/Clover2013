DB_NAME = 'sqlite.db'
APP_TRIGGER = ('id', 'kind', 'source', 'content', 'updated_at')
APP_TASK = ('id', 'user_id', 'trigger_id', 'action_id', 'parent_id', 'description', 'created_at', 'count', 'public')
APP_PENDING = ('id', 'action_id', 'user_id', 'content')
APP_ACTION = ('id', 'kind', 'source', 'destination', 'content')
AUTH_USER = ('id', 'user_name', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
APP_FUDANACCOUNT = ('id', 'username', 'password', 'user_id')

import sqlite3
con = sqlite3.connect(DB_NAME)

def execute(sql):
	return con.cursor().execute(sql)

def fetchById(table, id_):
	data = execute('select * from %s where id=%s' % (table, id_)).fetchone()
	return dict(zip(eval(table.upper()), data))

def insert(table, info):
	columns = ','.join(str(item[0]) for item in info.items())
	values = ','.join("'" + item[1] + "'"  if isinstance(item[1], str) else str(item[1]) for item in info.items())
	sql = "insert into %s (%s) values (%s)" % (table, columns, values)
	print sql
	execute(sql)

if __name__ == '__main__':
	test = {'action_id': 1, 'user_id': 1, 'content': 'hello'}
