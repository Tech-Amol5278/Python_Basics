# make flexible functions

# *args - to pass multiple arguments in function ( * operator)

# *args
    # args can be replaced by any word such as nums,i, k but for better practice keep using args only


# below function to add numbers, returns error since we are providing multiple arguements

def add_num(a,b):
    return(a + b)

print(add_num(4,5)) # this is okay 
# print(add_num(1,2,2,3)) # this returns error since we are passing more than 2 arguements


# TO handle this we can use *args , we can user too many arguements

def add_num_args(*args):
    print(type(args)) # data type of args is always tuple 
    print(args)
    return args

print(add_num_args(1,2,3,4,3,4,5,5,6))

   
   
