# Zip function
user_id = ['user1','user2']
names = ['Amol','Akshay','Vishal']

#  ('user1','Amol'),('user2','Akshay')

print(list(zip(user_id,names)))
print(dict(zip(user_id,names)))

# zip to create dictioanry from tuples

example = [('a',1),('b',2),('c',3)]
print(dict(example))

# we can only convert the list or tuples to dictionary which has 2 elements

name1 = ['ashish','rakeshh','niraj']
print(list(zip(user_id,names,name1)))
# print(dict(zip(user_id,names,name1)))  # this returns error






