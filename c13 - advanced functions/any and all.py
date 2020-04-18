# any and all functions

num1 = [2,4,6,8,10]
num2 = [1,2,3,4,5,6]


# to check and print if the number is true

# to check the evens in list num1
evens = []
def is_even(l):
    for i in l:
        evens.append( i%2 == 0)
    return evens   
    
print(is_even(num1)) 

# [True, True, True, True, True]  
# Above returned all true's, to check all the items are true. See below short code

print(all([True, True, True, True, True]))  ## this returns true, if all the values are true
print(all([True, True, False, True, True]))  ## this returns fllse, since not all values are true

# to check all the values are true using list comprehension
print(all([ i%2 == 0 for i in num1]))

# To check any of the value is true
print(any([True, True, False, True, True])) ## this returns true, if any single value is true

print(any([ i%2 == 0 for i in num1]))
