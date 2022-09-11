class Human:

    def __init__(self, first, last, age):
        self._first = first
        self._last = last

        self._age = age

    @property
    def age(self):  
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

if __name__ == '__main__':

    couple = Human('Walter','White',50)

    print(couple.age)

    couple.age = 5

    print(couple.age)
