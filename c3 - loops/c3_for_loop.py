# while loop 
# print("hello world") 10 times

########################################################################

# i = 1

# while i <= 10:
#     print("hello world")
#     i +=1

########### Example:1  For loop same program #######################################

for i in range(10):    ### range is 0 to 9 here 
    print("hello world")
    i += 1



for i in range(1,11):    ### range is 1 to 10 here 
    print("how r u")
    i += 1

####### Example:2 Sum from 1 to 10 ##############################

num = 10 
sum_num = 0
for i in range(num+1):
    sum_num += i
    i+=1

print(sum_num)


############ Example 3: 

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

#####

name = input("Enter user's name: ")
len_name = len(name)
print(len_name)

### getting unique letters from name ####
uq_name = ''
i = 0

for i in range(len_name):
    if name[i] not in uq_name:
        uq_name += name[i]
    i += 1

#### get letter count from name ##

for i in range(len(uq_name)):
    print(f"{uq_name[i]} : {name.count(uq_name[i])}")
    i += 1

