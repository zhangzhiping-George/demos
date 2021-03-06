from urllib import request, parse, error

print('Login to weibo...')
email = 'zzp_ly2008@163.com'


header_data = {
	'Origin': 'https://passport.weibo.cn',
	'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25',
	'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'
}
login_data = parse.urlencode([
	('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
	('savestate', '1'),
	('ec', ''),
	('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')]
)
req = request.Request(url='https://passport.weibo.cn/sso/login', data=login_data.encode('utf-8'), headers=header_data)
with request.urlopen(req) as f:
	print('Status: ', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' %(k, v))
	print('Data: ', f.read().decode('utf-8'))



