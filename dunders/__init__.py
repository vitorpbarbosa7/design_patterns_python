class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __str__(self):
        print(f'start {self.num} and end {self.end}')

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num +=1
            return self.num - 1 

if __name__ == '__main__':
    a,b = 2,5

    c1 = Counter(a,b)
    c2 = Counter(a,b)

    # Print using iter:
    # generator for c2 object 
    obj = iter(c2)
    try:
        while True:
            print('Counting', next(obj))
    except:
        print('over')
