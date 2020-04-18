# Function returning two values
# This always returns tuples

def func(int1,int2):
    add = int1 + int2
    mult = int1 * int2
    
    return add,mult

print(func(5,6))   # this will always retun in tuple

# but we can assign to diffrent variable, see below
add,multiply = func(5,6) 
print(add)
print(multiply)


