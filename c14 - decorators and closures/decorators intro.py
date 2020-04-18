# Decorators - enhance the functionality of other functions
# @ use for shortcut to call decorators
# example
# incase we want to print the line "this is awsome function" without channgng the below code



def decorator_func(any_func):
    def wrapper_func():
        print("This is awsome function")
        any_func()
    return wrapper_func

@decorator_func    ## before defining the function
def fn1():
    print('this is function 1')

@decorator_func 
def fn2():
    print('this is function 2')



fn1()
fn2()

# var = decorator_func(fn1)
# var()







