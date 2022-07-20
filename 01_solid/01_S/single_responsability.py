import numpy as np

def _mean(list_):
    # Compute Average
    print(f'the mean is {np.mean(list_)}')

def _max(list_):
    # Compute Max
    print(f'the max is {np.max(list_)}')

# add median function:


def math_operations(list_):
    _mean(list_)
    _max(list_)
    
if __name__ == '__main__':
    math_operations(list_ = [1,2,4,8,7])