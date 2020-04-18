# functions practice

# function to get the name as input and returs a last character.

# def last_char(name):
#     l_char = name[len(name)-1]
#     return l_char


# name = input("Enter your name: ")
# print(last_char(name))

# function to check odd or even
def odd_even(number):
    if number % 2 == 0:
        flag = "Entered number is EVEN"
    else:
        flag = "Entered number is ODD"
    return flag

def odd_even_1(number):
    if number % 2 == 0:
      return "Entered number is EVEN"
    return "Entered number is ODD"

def is_even(number):
    return number % 2 == 0 ### returns boolean value
    


num = input("Enter a number to check odd or even:")
num = int(num)
print(odd_even(num))
print(odd_even_1(num))
print(is_even(num))



