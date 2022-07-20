# decorator
def singleton(class_):
    # instances methods will be stored in a dict
    instances = {}

    #wrapper which adds/alters the class_ function
    def get_instance(*args, **kwargs):
        # if a instance is not in the set of instance, then we will add it 
        # to the set of instances
        if class_ not in instances:
            # add it
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    # return specific instance 
    return get_instance

# this class Database will be checked under the singleton created
# if it was not instantiated before, than it will be added to the instances dictionary
# presented in the function we are using to be the decorator

@singleton
class Database:
    # initializer should not be called twice
    def __init__(self):
        print('Loading database')

if __name__ == '__main__':
    # first call
    d1 = Database()
    # second call
    d2 = Database()
    print(d1 == d2)

    # we see that the instance was called only once