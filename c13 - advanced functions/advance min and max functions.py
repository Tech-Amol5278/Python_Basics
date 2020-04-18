# adavance min and max

names = ['Amol','jvfjdhf','adfadfafh','ag','hjsdgfysddgfgafdaj']

# to check the max and min length, we cannot use max.min, this returns incorrect results.see below

print(max(names))
print(min(names))

# max and min functions works only with int and float data types, while list has string elements

# Method 1  - using function as key 

def func(a):
    return len(a)   ## this returns length of the string

print(max(names, key=func))  # key - is the logic in which we tell interpreter how the max/min function should work
print(min(names, key=func))  # key - is the logic in which we tell interpreter how the max/min function should work

# Method 2  - using lambda expressions as key

print(max(names, key = lambda item: len(item)))  # key - is the logic in which we tell interpreter how the max/min function should work

################################################

students = {
    'harshit' : {'score' : 90,'age': 24},
    'mohit' : {'score' : 75,'age': 19},
    'rohit' : {'score' : 76,'age': 23}
}

students2 = [
    {'name':'harshit','score':90,'age':24},
    {'name':'mohit','score':95,'age':19},
    {'name':'rohit','score':76,'age':23}
]

# find the student which has highest score in students2

print(max(students2, key = lambda item: item.get('score') ))


















