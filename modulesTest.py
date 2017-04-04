import asyncio
import aiomysql

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test_example():
    conn = yield from aiomysql.connect(host='127.0.0.1', port=3306,
                                       user='root', password='123456',
                                       db='mysql', loop=loop)

    # create default cursor
    cursor = yield from conn.cursor()

    # execute sql query
    yield from cursor.execute("SELECT Host, User FROM user")

    # fetch all results
    yield from cursor.fetchall()
	

    # detach cursor from connection
    yield from cursor.close()

    # close connection
    conn.close()

loop.run_until_complete(test_example())

#===============================================================
# import json
# dict_a={'1':2, '2':'string', '3':['a','b'], '4':'青团 》 熊猫 ？'}
# json_a=json.dumps(dict_a, ensure_ascii=True, indent=4,sort_keys=True)
# print(json_a)
# json2dict_a=json.loads(json_a)
# print(json2dict_a)

# from io import StringIO
# io = StringIO('[1,2,"a","b"]')
# print(json.load(io))
#==================================================================
# import logging

# logging.basicConfig(level=logging.DEBUG,
				# format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
				# datefmt='%a, %d %b %Y %H:%M:%S',
				# filename='F:\loggingfilename',
				# filemode='w'
				# )
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('F:\loggingfilename11').addHandler(console)

# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')