# We use enumerate function with for loop to track the position of our item in iterable 

# how we can do this without using enumerate
names = ['abc','abcdchab','akjdbh']

pos=0
for i in names:
    print(f"{pos} --> {i}")
    pos += 1


# using enumerate 

for pos, i in enumerate(names):
    print(f"{pos} --> {i}")



# Define a function that takes two arguements 
# 1. List containing string
# 2. String that want to find in given list
# this function will return the index of the string in your list and if string is not present then return -1
# Note : use enumerate
# ######## Sol 

# def find_str(l,s):
#     pos = 0
#     if s in l:
#         for i in l:
#             if i == s:
#                 print('match found')
#         return pos
#         pos += 1
#     else: 
#         return -1


# print(find_str(['amol','ahahgd','vishal'],'vishal'))

# Using Enumerate function

def find_str2(l,s):
    pos = 0
    for pos,i in enumerate(l):
        if i == s:
           return pos
    return -1

         

print(find_str2(['amol','ahahgd','vishal'],'vishal'))






