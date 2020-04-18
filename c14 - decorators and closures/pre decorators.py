# You have to have complete understandings about the functions
# first class function / closures 
# then finally, we will learn about the decorators 


def square(a):
    ''' This is doc string. This is function is to get the square of the nums '''
    return a**2

s  = square

print(square(7)) # or
print(s(7))   # same thigs as above.


##  to print the doc string
print(square.__doc__)

