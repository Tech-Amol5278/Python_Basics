# Lambda expression practice 

# to check the no. is odd or even

def is_even(n):
    return n%2 == 0

print(is_even(7))    

# to check the no. is odd or even with lambda

is_even2 = lambda n: n%2 ==0

print(is_even2(6))    

# to get the last character from given string

last_char = lambda s : s[len(s)-1]

print(last_char('Amol'))

# to get the boolean if the length of given string is greter than 5

def is_bigger(s):
    return len(s) > 5

print(is_bigger('Vishal'))

# to get the boolean if the length of given string is greter than 5 with lambda

is_bigger2 = lambda s : len(s) > 5

print(is_bigger2('Vishal'))

# to get the boolean if the length of given string is greter than 5 with lambda
# using if else

# is_bigger3 = lambda s : print('True') if len(s) > 5 else 'False'  # incorrect way
is_bigger4 = lambda s : True if len(s) > 5 else False


# print(is_bigger3("Vishal"))

print(is_bigger4("Vishal"))









