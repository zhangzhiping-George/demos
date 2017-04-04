import hashlib

db = {}

def register(username, password):
	db[username] = hashlib.md5(username.encode('utf-8') + password.encode('utf-8') + 'salt'.encode('utf-8')).hexdigest()

def login(username, password):
	addSaltPasswd = hashlib.md5(username.encode('utf-8') + password.encode('utf-8') + 'salt'.encode('utf-8')).hexdigest()
	if addSaltPasswd == db[username]:
		print('welcome, %s' %username)
	else:
		print('Invalid username or password, please try again!\n')

register('user1', 'abcde123')
login('user1', 'abcde123')