# Validation for Int and Floats for a math functions
from functools import wraps
def math_validate(fn):
    @wraps(fn)
    def exec_func(*args):
        if all([type(arg) == int for arg in args]):
            return fn(*args)
        print('Please check the input first')
    return exec_func




@math_validate
def add_all(*args):
    sum1 = 0
    for arg in args:
        sum1 += arg
    return sum1


print(add_all(1,2,3,4,5))
print(add_all(1,2,3,4,5,'harshi'))  ## this wont work
# add_all(1,2,2,3)