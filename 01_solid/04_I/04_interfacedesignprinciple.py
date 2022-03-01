# The Machine interface is a class with all of those functions in only one
class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

# Inherent Class
# example: multi = MultiFunctionPrinter()
# multi.print()
# multi.fax()
# multi.scan()
class MultiFunctionPrinter(Machine):

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

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