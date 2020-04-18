# Output
# You are calling add function
# This function takes two numbers as argurments and return their sum 

from functools import wraps
def dec_fun(fn):
    @wraps(fn)
    def wr_fn(*args):
        print(f"You are calling {fn.__name__} function")
        print(f"{fn.__doc__}")
        return fn(*args)
    return wr_fn

@dec_fun
def add(a,b):
    '''This function get two numbers and return their sum'''
    return (a+b)

var = add(4,5)
print(var)

