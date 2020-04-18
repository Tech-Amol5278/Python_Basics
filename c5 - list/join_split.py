# split method 
# converts string into list

user_info = 'Amol 30'.split()
user1 = 'Akshay,30'.split(',')
name,age='Amol 30'.split()



print(user_info)
print(user1)
print(name)
print(age)


# join method
# converts list into string

user2 = ['harshit','24']
print(','.join(user2))

# below returs error because list contains int value
# user3 = ['harshit',25]
# print(','.join(user3))




