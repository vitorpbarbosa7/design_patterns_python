# The Machine interface is a class with all of those functions in only one
from abc import abstractmethod


class Machine:
    def __init__(self, document:str):
        self.document = document
    def print(self):
        print(f'{self.document} printed')
    def fax(self):
        print(f'{self.document} faxed')
    def scan(self):
        print(f'{self.document} scanned')

# Inherent Class
# example: multi = MultiFunctionPrinter()
# multi.print()
# multi.fax()
# multi.scan()
class MultiFunctionPrinter(Machine):

    def email(self):
        print(f'attach document {self.document}')

    # def print(self):
    #     pass

    # def fax(self):
    #     pass

    # def scan(self):
    #     pass

# This is way your OldFashionedPrinter can not inheret from Machine
class OldFashionedPrinter(Machine):
    def print(self, document):
        # here we can actually put something here, because the
        # old fashioned printer actually prints, as the Machine base class does 
        pass

    def fax(self, document):
        # But a old fashioned printer wouldn't print
        # so we could do absolutely nothing here 
        pass

    # But imagine that I declare an object from this class, and this funcitons are here, so, 
    # i will whink that it does really do something

''' Above code would be the correct way to do it'''
# Correct way to do it
class Printer:
    @abstractmethod
    # not implemented here
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    # not implemented here
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        # declare the action only here
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)
         # declare the action only here
        pass

    def scan(self, document):
        scan(document)
         # declare the action only here
        pass
''' End of implementation '''

''' Example of abstractmethod
import abc
class Shape(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def area(self):
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b
r = Rectangle(10,20)
print ('area: ',r.area())'''

if __name__ == '__main__':
    print('Base case machine')
    m = Machine('general machine')
    # call print 
    m.print()
    # call fax
    m.fax()
    # call scan
    m.scan()

    print('Multi function printer')
    multi = MultiFunctionPrinter('multi function machine')
    multi.print()
    multi.fax()
    multi.scan()
    multi.email()

    print('')



