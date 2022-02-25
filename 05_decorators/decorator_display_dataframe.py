# Interactive methods only work in jupyter notebook
# This is only a source code to implementation
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

data = pd.read_csv('data/iris.csv')

def disp(f,ri:int = None, ci:int = None, rf:int = 6, cf:int = None):
    '''
    Decorator to configure different number of rows and columns locally, in execution time, but return 
    to original desired default values, immedially after execution
    
    Parameters
    ---------------
    ri: Row numbers to execute at display dataframe action
    ci: Column numbers to execute at display dataframe action
    rf: Default number of rows to keep after execution of display dataframe
    cf: Default number of columns do keep after execution of display dataframe
    '''
    def modified(dataframe:pd.DataFrame):
        pd.set_option('display.max_rows', ri)
        pd.set_option('display.max_columns', ci)
        f(dataframe)
        pd.set_option('display.max_rows', rf)
        pd.set_option('display.max_columns', cf)
    return modified
        
# lets decorate the display dataframe method, so that we can control how many rows and cols we can show
@disp
def dp(dataframe):
    '''
    Method to display dataframe
    '''
    from IPython.display import display
    display(dataframe)

dp(data)

# Another way

def decodisp(ri:int = None, ci:int = None, rf:int = 6, cf:int = None):
    def disp(f):
        '''
        Decorator to configure different number of rows and columns locally, in execution time, but return 
        to original desired default values, immedially after execution

        Parameters
        ---------------
        ri: Row numbers to execute at display dataframe action
        ci: Column numbers to execute at display dataframe action
        rf: Default number of rows to keep after execution of display dataframe
        cf: Default number of columns do keep after execution of display dataframe
        '''
        def wrapper(dataframe:pd.DataFrame):
            pd.set_option('display.max_rows', ri)
            pd.set_option('display.max_columns', ci)
            f(dataframe)
            pd.set_option('display.max_rows', rf)
            pd.set_option('display.max_columns', cf)
        return wrapper
    return disp

def dpb(dataframe):
    '''
    Method to display dataframe
    '''
    from IPython.display import display
    display(dataframe)

decodisp(ri = 2,ci = 4)(dpb)(data)