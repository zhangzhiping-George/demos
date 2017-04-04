import asyncio
import logging
logging.basicConfig(level=logging.DEBUG,
				format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
				#filename='F:\pythonproj\awesome-python3-webapp\logs\messages.log'
				)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

def hello(req):
	text = '<h1>hello, %s!</h1>' % req.match_info['nam']
	return web.Response(body=text.encode('utf-8'), content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{nam}', hello)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
		




































