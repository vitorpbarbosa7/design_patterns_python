class Event(list):
	# This event accepts 'anything'
	# instance behave like functions, hence, can be called
	def __call__(self, *args, **kwargs):
		 for item in self:
			 item(*args, **kwargs)

class Person:
	def __init__(self, name, address):
		self.name = name
		self.address = address
		# composition ?
		self.falls_ill = Event()
	
	def catch_a_cold(self):
		# chamando os eventos
		self.falls_ill(self.name, self.address)

def call_doctor(name, address):
	print(f"{name} needs a doctor at {address}")

def call_ambulance(name, address):
	print(f"Call 911")

if __name__ == '__main__':
	person = Person('Sherlock', '221B Baket St')
	
	# calls event
	person.falls_ill.append(call_doctor)
	person.falls_ill.append(call_ambulance)
	
	# event notification calls the event Implementation
	person.catch_a_cold()
	
