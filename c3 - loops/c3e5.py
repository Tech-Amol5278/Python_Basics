# ask user for name 
# Example - Amol Chavan
# print count of each words
# output: 
#     A : 1
#     m : 1
#     o : 1
#     l : 1
#       : 1
#     C : 1
#     h : 1
#     a : 2
#     v : 1
#     n : 1

########################### Sol #################################################################

name = input("Please enter your name: ")
### get unique letters in name ########
uq_name = ''
i = 0
while i < len(name):
    if name[i] in uq_name:
        i += 1
    else:
        uq_name = uq_name + name[i]
        i += 1
### count unique letters in name 

i = 0
while i < len(uq_name):
    print(f"{uq_name[i]} : {name.count(uq_name[i])}")
    i += 1




