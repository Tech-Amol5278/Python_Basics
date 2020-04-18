# Dictionaries Intro
# Why we use Dictionaries?
#     Because of the limitations of lists, lists are not enough to represent real data.

# Example :
# user = ["Amol",'30',['coco','kimi no na wa'],['awakening','fairy tale']]

# Above list contains user's name, age, favourite movies and favourite tunes 
# But this is not a good way to store or represent data

# What are dictionaries?
#     Unordered collection of data in key : value pair 

# How to create dictionaries?
    # Method 1
user = {'Name' : "Amol",'Age' : 30}
print(user)
print(type(user))

    # Method 12
user1 = dict(name="Amol",age=30)
print(user1)
print(type(user1))

# Accessing data from dictionaries 
# Unlike lists and tuple, we cannot access the data from dictionaries, because dictionaries are unordered hence does not use indexes
# Instead, we can use keys to access data, check below

print(user1['name'])   ## note: keys are case sensisitive
print(user1['age'])

# Which type of data a dictionary can store?
# anything

user_info = {
    'name' : 'Amol',
    'age' : 29,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tale'],
}

print(user_info['fav_movies'])

# How to add data into empty dictinary
user_info2={}
user_info2['name'] = 'Amol'
user_info2['age'] = 20

print(user_info2)




 










