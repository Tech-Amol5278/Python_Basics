# closures practice  

# square
# cube

# instead of creating two separate functions for square and cube, we can make a closure which can 
# we have already done this using *args
# Try this with closures

def to_power(x):
    def calc_power(n):
       return n**x 
    return calc_power  ## do not add () after this, cause this will exeucte the function but due to missing argeument it will return the error

cube = to_power(3)
square = to_power(2)

print(cube(3))  ## to get the cube
print(square(8))  ## to get the square








