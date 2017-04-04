## -*- coding = UTF-8 -*-
# '''this is the place to write docs'''
'''觉得这些东西都好难啊！！！，所以要感觉需要学的慢一点才能学会一样，错！！！ 快点，要更快点！！！ 东西是不断地反复练习中技能得以提升的，不是在每一步里蹉跎好久，没有意义的，体验差，效率低，没效果！！！ 改！！！ 快速前进，再回过头来练习！！！ 否则什么都干不了，哪还有perfect而言！！！'''
'''不要因为这样的小事情气馁，总是有困难才是正常的，遇到的气馁的事情太多的原因么，干什么都特别容易气馁，绝对不应该这样，不能这样的，勇于面对困难，这些困难是正常的，感到困难并不是自己做的差，自己做的并不差，遭遇让人心痛，自己做的不差，并勇于克服困难才能真正的帮助自己走出困境，走上人生巅峰的'''

'''向前走，勇敢地，绝不回头的向前走！'''
'''教育家Maria Montessori 的理念： 纪律应该来自自由，而不是约束。那些被说教、强迫、洗脑、威胁、惩罚出来的‘乖学生’不是守纪律，而是被麻痹、被毁掉了。当一个学生拥有自由，理解他是自己的主人，然后选择去做他应做的事，不做他不应做的事，这样的纪律才有价值。'''
'''
我的观察和实践告诉我，成绩优秀的学生，都把学习{sincerely}当成日常的习惯。
'''
#__author__ = 'George'

# def _private_1(name):
	# print('Hi, %s' %name)
	
# def _private_2(name):
	# print('Hsi,%s' %name)
	
# def greeting(name):
	# if len(name) > 3:
		# return _private_1(name)
	# else:
		# return _private_2(name)
		
# greeting('abc')

# class (object):
    # def __getitem__(self, n):
        # if isinstance(n, int): # n是索引
            # a, b = 1, 1
            # for x in range(n):
                # a, b = b, a + b
            # return a
        # if isinstance(n, slice): # n是切片
            # start = n.start
            # stop = n.stop
            # if start is None:
                # start = 0
            # a, b = 1, 1
            # L = []
            # for x in range(stop):
                # if x >= start:
                    # L.append(a)
                # a, b = b, a + b
            # return L
# f = Fib()
# f[0:5]

# import os
# import sys 

# def rsearch(path, word):
	# for x in os.listdir(path):
		# fp = os.path.join(path, x)
		# if word in x: print(os.path.abspath(fp))
		# else:
			# if os.path.isdir(fp):
				# rsearch(fp, word)
# if __name__ == '__main__':
	# rsearch(sys.argv[1],sys.argv[2])

# from multiprocessing import Process, Queue

# import os, time, random

# def write(q):
	# print('Process to write: %s' %os.getpid())
	# for value in ['A', 'B', 'C']:
		# print('Put %s to queue' % value)
		# q.put(value)
		# time.sleep(1)
		
# def read(q):
	# print('Process to read: %s' %os.getpid())
	# while True:
		# value = q.get()
		# print('Get %s from queue.' % value)
	

# if __name__== '__main__':
	# q = Queue()
	# pw = Process(target=write, args=(q,))
	# pr = Process(target=read, args=(q,))
	# pw.start()
	# pr.start()
	# pw.join()
	# pr.terminate()


# import random, time, queue
# from multiprocessing.managers import BaseManager

# task_queue = queue.Queue()
# result_queue = queue.Queue()

# class QueueManager(BaseManager):
	# pass

# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: task_queue)

# manager = QueueManager(address=('', 5000), authkey=b'abc')
# manager.start()

# task = manager.get_task_queue()
# result = manager.get_result_queue()

# for i in range(10):
	# n = random.randint(0, 1000)
	# print('Put task %d...' %n)
	# task.put(n)
	
# print('Try get results...')

# for i in range(10):
	# r = result.get(timeout=10)
	# print('Result: %s' %r)
	
# manager.shutdown()
# print('master exit.')

 ## -*- coding: utf-8 -*-
#-*- coding: gbk -*-
# import base64

# def safe_base64_decode(s):

    # x = len(s) % 4
    # if  x != 0:
        # s = s + b'=' *(4-x)
    # return base64.b64decode(s)
#测试:
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# print('Pass')


# class Query(object):

    # def __init__(self, name):
        # self.name = name

    # def __enter__(self):
        # print('Begin')
        # return self

    # def __exit__(self, exc_type, exc_value, traceback):
        # if exc_type:
            # print('Error')
        # else:
            # print('End')

    # def query(self):
        # print('Query info about %s...' % self.name)
		
		
# with Query('Bob') as q:
	# q.query()

# from contextlib import contextmanager

# @contextmanager
# def tag(name):
	# print("<%s>" %name)
	# yield
	# print("<%s>" %name)
	
# with tag("h1"):
	# print("hello")
	# print("world")



# class Query(object):
	
	# def __init__(self, name):
		# self.name = name
		
	# def query(self):
		# print('Query info about %s...' %self.name)
		
# @contextmanager
# def create_query(name):
	# print('Begin')
	# q = Query(name)
	# yield q
	# print('End')
	
# with create_query('Bob') as q:
	# q.query()
	
	
# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):
    # def start_element(self, name, attrs):
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    # def end_element(self, name):
        # print('sax:end_element: %s' % name)

    # def char_data(self, text):
        # print('sax:char_data: %s' % text)

# xml = r'''<?xml version="1.0"?>
# <ol>
    # <li><a href="/python">Python</a></li>
    # <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''

# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)
	
	
# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):

    # def handle_starttag(self, tag, attrs):
        # print('<%s>' % tag)

    # def handle_endtag(self, tag):
        # print('</%s>' % tag)

    # def handle_startendtag(self, tag, attrs):
        # print('<%s/>' % tag)

    # def handle_data(self, data):
        # print(data)

    # def handle_comment(self, data):
        # print('<!--', data, '-->')

    # def handle_entityref(self, name):
        # print('&%s;' % name)

    # def handle_charref(self, name):
        # print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
	# <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')
#!/usr/bin/python
# -*- coding: utf-8 -*-

# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
	# def __init__(self, master=None):
		# Frame.__init__(self, master)
		# self.pack()
		# self.createWidgets()
	
	# def createWidgets(self):
		# self.nameInput = Entry(self)
		# self.nameInput.pack()
		# self.alertButton = Button(self, text='Hello', command = self.hello)
		# self.alertButton.pack()
	
	# def hello(self):
		# name = self.nameInput.get() or 'world'
		# messagebox.showinfo('Message', 'Hello, %s' %name)
		
		
# app = Application()
# app.master.title('Hello world')
# app.mainloop()
	
	
# import socket

# 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# buffer = []
# while True:
    # 每次最多接收1k字节:
    # d = s.recv(1024)
    # if d:
        # buffer.append(d)
    # else:
        # break
# data = b''.join(buffer)
# s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
    # f.write(html)
	
# -*- coding: utf-8 -*-
# from email import encoders
# from email.mime.text import MIMEText
# from email.header import Header
# from email.utils import parseaddr, formataddr
# from email.mime.multipart import MIMEMultipart

# import smtplib

# def  _format_addr(s):
	# name, addr = parseaddr(s)
	# return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input("SMTP SERVER: ")

# msg = MIMEMultipart()
# msg["From"] = _format_addr("Python爱好者 <%s>" % from_addr)
# msg["To"] = _format_addr("管理员 <%s>" % to_addr)
# msg["Subject"] = Header("来自SMTP的问候...", 'utf-8').encode()
# msg.attach(MIMEText('hello, send by python...', 'plain', 'utf-8'))
# att1 = MIMEText(open('demo.py', 'rb').read(),'base64','utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="attfile1"'
# msg.attach(att1)

# with open('sina.html', 'rb') as f:
	# mime = MIMEBase('text','plain', filename='sina.html')
	# mime.add_header('Content-Disposition', 'attachment', filename='sina.html')
	# mime.add_header('Content-ID', '<0>')
	# mime.add_header('X-Attachment-Id', '0')
	# mime.set_payload(f.read())
	# encoders.encode_base64(mime)
	# msg.attach(mime)

# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.starttls()
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
	# return '<h1>Home</h1>'
	
# @app.route('/signin', methods=['GET'])
# def signin_form():
    # return '''<form action="/signin" method="post">
              # <p><input name="username"></p>
              # <p><input name="password" type="password"></p>
              # <p><button type="submit">Sign In</button></p>
              # </form>'''
			  
# @app.route('/signin', methods=['POST'])
# def signin():
	# if request.form['username'] == 'admin' and request.form['password'] == 'passwd':
		# return '<h3>Hello, POST admin!</h3>'
	# return '<h3>Bad username or password.</h3>'
	
# if __name__ == '__main__':
	# app.run()

#return 0

# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
	# return render_template('homt.html')
	
# @app.route('/signin', methods=['GET'])
# def sign_form():
	# return render_template('form.html')
	
# @app.route('/signin', methods=['POST'])
# def signin():
	# username = request.form['username']
	# password = request.form['password']
	# if username == 'admin' and password == 'password':
		# return render_template('sign-ok.html', username = username)
	# return render_template('form.html', message='Bad username or password', )

# if __name__ == '__main__':
	# app.run()


# import asyncio

# @asyncio.coroutine
# def wget(host):
	# print('wget %s...' %host)
	# connect = asyncio.open_connection(host, 80)
	# reader, writer = yield from connect
	# header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' %host
	# writer.write(header.encode('utf-8'))
	# yield from writer.drain()
	# while True:
		# line = yield from reader.readline()
		# if line == b'\r\n':
			# break
		# print('%s header > %s' %(host, line.decode('utf-8').rstrip()))
	# writer.close()
	
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", '/', index)
    app.router.add_route("GET", '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
	
#return 0

# class Reverse:
	# def __init__(self, data):
		# self.data = data
		# self.index = len(data)
	# def __iter__(self):
		# return self
		
	# def __next__(self):
		# if self.index == 0:
			# raise StopIteration
		# self.index = self.index - 1
		# return self.data[self.index]
		
# rev = Reverse('abc')
# print(iter(rev))
# for char in rev:
	# print(char)

# return 0


# class Chain(object):
	
	# def __init__(self, path=''):
		# self._path = path
	# def __getattr__(self, path):
		# return Chain('%s/%s' %(self._path, path))
	# def __str__(self):
		# return self._path
	# __repr__ = __str__

# c = Chain()	
# print(Chain().user.login)
# print(c.name)






















































































