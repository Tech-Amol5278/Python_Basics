# get the time taken while executing the function using decorators
import time
from functools import wraps
def calc_time(fn1):
    @wraps(fn1)
    def exec_func(*args):
        print(f"You are calling {fn1.__name__}")
        t1 = time.time()
        returned_value = fn1(*args)
        t2 = time.time()
        print(f"Function {fn1.__name__} took {t2-t1} time")
        return returned_value
    return exec_func

@calc_time
def get_sq(n):
    return n**2

print(get_sq(5))

def get_sq_range(n):
    return [i**2 for i in range(1,n+1)]

print(get_sq_ranges(5))



get_sq(5)



