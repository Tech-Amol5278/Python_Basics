# add and delete data 

user_info = {
    'name' : 'Amol',
    'age' : 29,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tale'],
}

# how to add data
user_info['fav_songs'] = ['song1','song2']


# POP method (When working with dictionaries, pop must have one argument)

popped_item = user_info.pop('fav_songs')
print(f"Popped item is {popped_item}")

print(user_info)

# POPitem method : removes last key, value

popped_item = user_info.popitem()
print(user_info)
print(f"Popped item is {popped_item}")
print(type(popped_item))
