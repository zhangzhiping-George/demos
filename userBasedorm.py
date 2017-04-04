# from orm import Model, StringField, IntegerField

# class User(Model):
	# __table__ = 'users'
	
	# id = IntegerField(primary_key=True)
	# name = StringField()
	# def show(self):
		# print(1, '__mappings__:', self.__mappings__)
		# print(2, '__table__:', self.__table__)
		# print(3, '__primary_key__:', self.__primary_key__)
		# print(4, '__fields__:', self.__fields__)
		# print(5, '__select__:', self.__select__)
		# print(6, '__insert__:', self.__insert__)
		# print(7, '__update__:', self.__update__)
		# print(8, '__delete__:', self.__delete__)
# user = User(id=123, name='Jack')
# user.show()
# user.insert()
# users = User.findAll()
# print(users)


import orm, asyncio
from models import User, Blog, Comment

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
	yield from orm.create_pool(host='localhost', port=3306, user='www-data', password='www-data', db='awesome', loop=loop)
	u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
	yield from u.save()

loop.run_until_complete(test())
loop.close()