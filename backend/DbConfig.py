DB_NAME = 'sqlite.db'
APP_TRIGGER = ('id', 'kind', 'source', 'content', 'updated_at')
APP_TASK = ('id', 'user_id', 'triger_id', 'action_id', 'parent_id', 'description', 'created_at', 'count', 'public')
APP_PENDING = ('id', 'action_id', 'done', 'content')
APP_ACTION = ('id', 'kind', 'source', 'destination', 'content')
AUTH_USER = ('id', 'user_name', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
APP_FUDANACCOUNT = ('id', 'username', 'password', 'user_id')
