def decorator_failure(func):
    def func_wrapper(*args, **kwargs):
        try:
           return func(*args, **kwargs)
        except Exception as e:
            msg = f'Function failed \n'
            msg_exception = f'exception: {e}'
            print(msg + msg_exception)
            return None
    return func_wrapper

@decorator_failure
def functionality(number, character):

    print(f'{number + character}')

if __name__ == '__main__':

    NUMBER = '2'
    CHARACTER = 6
    functionality(NUMBER, CHARACTER)