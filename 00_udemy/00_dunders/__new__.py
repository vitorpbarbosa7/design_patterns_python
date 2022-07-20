
# don't forget the object specified as base
class A(object):
    def __new__(cls):
         print("Creating instance")
         return super(A, cls).__new__(cls)
  
    def __init__(self):
        print("Init is called")

         
class B(object):
    def __new__(cls):
        print("Creating instance")
  
    # It is not called
    def __init__(self):
        print("Init is called")
  
if __name__ == '__main__':
    print('A class')
    A()
    print('B class')
    B()


