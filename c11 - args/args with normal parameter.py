# *args with normal parameters
# when using *args not mandatory to pass arguements 
# define a function for multiplication of given numbers

def multi_func(*args):
    multy_num = 1
    for i in args:
        multy_num *= i
    return multy_num

print(multi_func(4,2,3,4,6,7))

# If we pass normal parameter with args

def multi_func(n,*args):
    multy_num = 1
    for i in args:
        multy_num *= i
    return multy_num

print(multi_func(5,2,3,4,6,7)) # this will exclude 5 from args because 5 is the normal arguement which is not part of the args


