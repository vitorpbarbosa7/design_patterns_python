from __future__ import annotations 
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
	'''
	Subject interface
	Methods of managing subscribrers
	'''

	@abstractmethod
	def attach(self, observer: Observer) -> None:
		'''
		Attach an observer to the subject
		'''

	def detach(self, observer: Observer) -> None:
		'''
		Detaches observer from the subject
		'''

	def notify(self) -> None:
		'''
		Notify all observers about an event
		'''


class ConcreteSubject(Subject):
	'''
	The Subject holds states, and notifies observers when state changes
	'''

	_observers: List[Observer] = []

	def __init__(self, state):
		self._state = state

	def attach(self, observer: Observer) -> None:
		print("Subject: Attached an observer")
		self._observers.append(observer)

	def detach(self, observer: Observer) -> None:
		print("Subject: Detached an observer")
		self._observers.remove(observer)

	def emergency_call(self):
		EMERGENCY = 'emergency_call'
		self.notify(EMERGENCY)

	def warning_call(self):
		REUNION = 'reunion'
		self.notify(REUNION)

	def notify(self, message) -> None:
		''' trigger an method present in observer'''
		
		print("Subject: Notifying observers")
		for observer in self._observers:

			# pass as argument, itself, to the observer method, interesting
			observer.update(self, message)


class Observer(ABC):
	
	@abstractmethod
	def update(self, subject: Subject, message:str) -> None:
		''' Receives update from subject '''


class ConcreteObserverA(Observer):
	def update(self, subject: Subject, message:str) -> None:
		if subject._state < 3:
			print(f"ConcreteObserverA: Reacted to the event: {message}")

class ConcreteObserverB(Observer):
	def update(self, subject: Subject, message:str) -> None:
		if subject._state > 3:
			print(f"ConcreteObserverB: Reacted to the event: {message}")



if __name__ == "__main__":
	# client's code

	observer_a = ConcreteObserverA()
	observer_b = ConcreteObserverB()

	subject = ConcreteSubject(5)

	subject.attach(observer_a)
	subject.attach(observer_b)

	subject.emergency_call()
	subject.warning_call()

 

			





		
