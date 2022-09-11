import time

def time_it(func):
	def wrapper():
		start = time.time()
		func()
		end = time.time()
		print(f'{func.__name__} took {int(end-start)*1000}ms')
	# the function wrapper returned
	return wrapper

@time_it
def some_op():
	print('Starting op')
	time.sleep(1)
	print('We are done')
	return 123

if __name__ == '__main__':
	some_op()
