'''
Adicionar uma funcionalidade sem perder as funcionalidades do objeto original

O que garante a funcionalidade eh a chamada do getattr, que vai atras do objeto original "menor" para subscrever o (nao existente?) do objeto "maior" que engloba o "menor"
'''

class FileWithLogging:
	def __init__(self, file):
		self.file = file

	def writelines(self, strings):
		self.file.writelines(strings)
		print(f'wrote {len(strings)} words')

	# 	# quando for iterar sobre esse FileLogging, iterar sobre o file
	# def __iter__(self):
	# 	return self.file.__iter__()
	
	# def __next__(self):
	# 	return self.file.__next__()
	
	# maneira de herdar metodo write tambem para este FileWithLoggin
	# when externally using the getattr build-in python function, it will respect this:
	# ao inves de pegar o atributo write do FileWithLogging, pega o atributo write do file, que foi passado no 👷 
	def __getattr__(self, item):
		# pegar do file, do subclass, e nao do sup class (?) o attribute de item
		return getattr(self.__dict__['file'], item)

	# def __setattr__(self, key, value):
	# 	if key == 'file':
	# 		self.__dict__[key] = value
	# 	else:
	# 		setattr(self.__dict__['file'], key)

	# def __delattr__(self, item):
	# 	delattr(self.__dict__['file'], item)

if __name__ == '__main__':
	file = FileWithLogging(open('hello.txt', 'w'))
	file.writelines(['hello', 'world','three'])
	file.writelines(['foo', 'bar','tar'])
	file.write('')
	file.close()
