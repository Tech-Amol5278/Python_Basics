# in keyword and iterations in dictionary


user_info = {
    'name' : 'Amol',
    'age' : 29,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tale'],
}

# check if Key exists in dictionary 

if 'nae' in user_info:
    print("Given key exists")
else:
    print("Given key not available")

# check if Value exists in dictionary
    # if key is known

if user_info['name'] == 'Amol':
    print("Given Value exists")
else:
    print("Given Value not available")

    # if key is unkown

if 'Amol' in user_info.values():
    print("Given Value exists")
else:
    print("Given Value not available")

## Loops in dictionaries
    # to print only keys

for i in user_info:
    print(i)

    # one more way to get/print only values using only values method

user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))   ##  type: dict_keys

    # to print only Values


for i in user_info.values():
    print(i)

    # one more way to get/print only values using only values method

user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))   ##  type: dict_values


# Items method
# this returns the data from dictionary in items data type 
user_items = user_info.items()
print(user_items)
print(type(user_items))     ##  type: dict_items 
# dict_items([('name', 'Amol'), ('age', 29), ('fav_movies', ['coco', 'kimi no na wa']), ('fav_tunes', ['awakening', 'fairy tale'])])

for i, j in user_info.items():
    print(f"Key is {i} and Value is {j}")






















