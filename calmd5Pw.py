import hashlib
md5 = hashlib.md5()
def cal_md5(passwd):
	md5.update(passwd)
	md5_passwd = md5.hexdigest()
	print('md5_passwd of passwd %s is %s' %(passwd, md5_passwd))

pw='abcde123'
cal_md5(pw.encode('utf-8'))