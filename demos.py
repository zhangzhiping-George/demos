# def power(x, n):
	# s = 1
	# while n > 0:
		# n = n-1
		# s = s*x
	# return s
	
# print(power(5,2))

# def enroll(name, gender, city='Shenzhen'):
	# print('name:', name)
	# print('gender:', gender)
	# print('city:', city)

# enroll('Sarach', 'F', 'Beijing')
# enroll('Sarach', 'F')

# def add_end(L=None):
	# if L is None:
		# L = []
	# L.append('END')
	# return L
	
# print(add_end(['sadf',]))

# def calc(*numbers):
	# sum = 0
	# for n in numbers:
		# sum = sum + n*n
	# return sum

# print(calc(*[2,4,6]))
# print(calc(*(1,3,5,7)))
# print(calc(1,3,5,7))


# def person(name, age, **kw):
	# print('name:',name, 'age:',age, 'other:', kw)
	
# extra = {'city': 'BJ', 'job': 'Engineer'}

# person('Bob', 35, city='Beijing', gender='X')
# person('Bob', 35, **extra)

# def person(name, age, *args, city='BJ',job):
	# print('name:',name, 'age:',age, args, 'city:', city, 'job:', job)
	
# person('Jack', 24, 'anythingxx', 'testcity',   job='Engineer')


# def fact(n):
	# if n == 1:
		# return 1
	# return  n*fact(n-1)
	
# print(fact(1))
# print(fact(5))


# def _odd_iter(): #此函数生成一个奇数序列
	
	# n = 1
	# while True:
		# n = n + 2
		# yield n
		# if n > 1000:
			# break
	
# it = list(_odd_iter())

# for n in it:
	# print(n) # 无限循环
		
# def _not_divisible(n):
	# return lambda x: x % n > 0
	
# def primes():
	# yield 2
	# it = _odd_iter()
	# while True:
		# n = next(it) 
		# yield n
		# it  = filter(_not_divisible(n), it)
		

# for n in primes():
	# if n < 100:
		# print(n)
	# else:
		# break
	


import functools

def decorator0(method):
	def decorator(func):
		@functools.wraps(func)
		def twrapper(*args, **kw):
			print("begin call")
			print('%s %s():' %(method, func.__name__))
			print("end call")
			return func(*args, **kw)
		return twrapper
	return decorator
	
@decorator0('execute')

def testFunc():
	print("I'm being called now")
	
testFunc()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	





































