# Debugging:
    # process of finding and resolving the problems within a computer  program that prevents correct operation
    # of software or a system

# Why Debugging?
    # 1. Our programs is not running and causing unexpected errors
    # 2. Our program is working but insights are not as exepected

# Steps for Debugging;
    # 1. set trace
        # l : to know the line on which code execution paused   
        # n : execute next line
        # variable_name: to know the values passed in variable enter the variable name and press enter
        # c : to continue with the program execution
        # q : quit and exit program exectution

    # 2. Execute code line by line 

# This requires a module to imported 
    # Module: PDB 

# try below example  which returns below error
    # TypeError: can only concatenate str (not "int") to str

# name = input("Please enter your name: ")
# age = input("Please enter your age: ")
# print(f"Hello {name},your age is {age}")
# age2 = age + 5
# print(f"You will be {age2} after five years")

####  sol ##
import pdb  # import pdb module

pdb.set_trace()
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f"Hello {name},your age is {age}")
age2 = age + 5
print(f"You will be {age2} after five years")



