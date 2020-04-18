# 

def decorator_func(any_func):
    def wrapper_func(*args,**kwargs):
        print("This is awsome function")
        return any_func(*args,**kwargs)
    return wrapper_func

@decorator_func    ## before defining the function
def fn1(a):
    print(f'this is function with argument {a}')

# this will retrun error if we pass the argument, since in decorator_func we have not given a parameter 
# to pass the arguements. Hence the decorator function needs to be modified .
fn1(5)

@decorator_func
def add(a,b):
    return a+b 

add(4,5)
print(add(4,5))
