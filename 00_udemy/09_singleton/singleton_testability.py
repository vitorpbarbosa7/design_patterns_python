import unittest
import os 
cwd = os.getcwd()   
print(cwd)

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).\
                __call__(*args, **kwargs)   
        return cls._instances[cls]

# when it is initialized, calls the database
# the ideia is a very useful approach to data science pipelines
class Database(metaclass = Singleton):
    def __init__(self):
        # you want to load the database only once
        self.population = {}
        path = 'data/01_raw/'
        f = open(path + 'capitals.txt', 'r')
        lines = f.readlines()
        f.close()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] =\
                int(lines[i+1].strip())

class ConfigurableRecordFinder:
    def __init__(self, db):
        # making it possible to override the database
        self.db = db

    # inject the database here
    def total_population(self, cities):
        result = 0
        # is directly tied to the database
        for c in cities:
            result += self.db.population[c]
        return result

# Now I can use any database
class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]





class SingletonRecordFinder:
    ''' This record finder is using a specific Database, which is dangerous '''
    def total_population(self, cities):
        result = 0
        # is directly tied to the database
        for c in cities:
            result += Database().population[c]
        return result

# Unit Test

class SingletonTests(unittest.TestCase):

    # Here you write your tests with asserts for example
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1,db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Seoul','Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(175_000_00 + 174_000_00, tp)

    # allows for test with dummydatabase
    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        ''' This test is a superior test because is not tied up
        to the Database, it can be the singleton dabase, but also 
        can be overrided'''
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(3,crf.total_population(['alpha','beta']))

          
if __name__ == '__main__':
    # Execute any subclass associated with base class unittest
    unittest.main()
