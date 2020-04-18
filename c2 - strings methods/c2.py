#### CHTAPTER 2 : STRINGS #############
# strings  = collection of characters inside single quotes or double quotes


first_name = "Amol"
last_name = "Chavan"

full_name = first_name +" "+ last_name

print(full_name)
#####
# print (first_name+3)   ## error
print (first_name + "3")   ## noerror
print(first_name + str(3))   ## noerror
print (first_name * 3)   ## noerror
##########################################
## User Input
## Input function(always takes input in string format)

name = input("Type your name: ")
print("Hello "+ name)

age = input("What is your age: ")
print("Your age is "+ age)
#### Tut: 19 #########################
num1  = input("Enter first number: ")
num2  = input("Enter second number: ")
total = num1 + num2  ## Incorrect output will be concatenated
print(total)
print("which is incorrect, lets try one more time with correct code")
num3  = int(input("Enter first number: "))
num4  = int(input("Enter second number: "))
total = num3 + num4  ## Incorrect output will be concatenated
print(total)
####### Data type conversions ######

# str 
# 4 ----> "4"

# int 
# "4" -----> 4

# float
# "4" -----> 4.0

# note: int + float = float
###### Tut: 20 ######
## multuple varialbles
name, age = "Amol","28"
print("Hello " + name + " Your age is " + age)

x=y=z=1
print(x+y+z)
#### Tut: 21 ##########
## accepting multiple inputs from user in one line
name,age = input("Enter you name and age, separated by comma:").split(",")

print(name)
print(age)
 
 #### Tut: 22 ###########
 # Strig formatting

name =  "Amol"
age = 29
print("hello " + name + " your age is " + str(age)) #ugly syntax
print("Lets try the same using optimized code using place holders")
print("hello {} your age is {} ".format(name,age))




















