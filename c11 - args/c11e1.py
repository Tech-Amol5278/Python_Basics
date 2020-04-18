# # Define a function 

# input - num, iterable(tuple or list)

# Example -
# nums = [1,2,3]
# ti_power(3,*nums)

# Output - 
# [1,8,27]

# if user did not pass the list then return a message that "Hey, you did not pass the List"

# Note - Use List comprehension

##### 

# if n != '' or args != '':
       
def to_power(n,*args):
    if args:
        power_list = [i**n for i in args ]
        return power_list
    else:
        print("You didnt pass an args")
    

nums = [1,2,3]
print(to_power(2))



