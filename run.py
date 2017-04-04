# -*- coding: utf-8 -*-
# import sys
# from subprocess import *

# p = Popen("python subprocessTest.py", stdin=PIPE, stdout=PIPE, shell=True)

# for line in sys.stdin:
	# p.stdin.write(line.encode('utf-8'))
	# p.stdin.flush()
	# output = p.stdout.readline()
	# sys.stdout.write(output.decode('utf-8'))
	
# ? 字符串编解码的方法
# ? read, readline, readlines

from subprocess import Popen, PIPE
import time, sys

p = Popen('ping baidu.com', shell=True, stdin=PIPE, stdout=PIPE)

while p.poll() == None:
	print(p.stdout.readline())
	time.sleep(5)
#print(p.stdout.readlines())
sys.stdout.write(str(p.stdout.readlines()))
time.sleep(2)
print('return code: %s' %p.returncode)