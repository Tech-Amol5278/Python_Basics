# Python custom exceptions
# why custom exceptions
    # ans: to increase the readibility of code


# def validate(name):
#     if len(name) < 8:
#         raise ValueError ('name too short, pls tryy with diffrent name')

# username = input("Please enter your name: ")
# validate(username)
## or ##
# we can make our error , see below

class NameShortError(ValueError): ## Inherited value error class
    pass

def validate1(name):
    if len(name) < 8 :
        raise NameShortError


username1 = input("Please enter your name again to check with nameshort error: ")
validate1(username1)