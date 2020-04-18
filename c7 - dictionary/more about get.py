# more about get, two same keys in dictionary

user = {'name':'Amol','age' : 30}

print(user['name'])
print(user.get('names','Not found !!'))

user = {'name':'Amol','age' : 30,'age':'50'} # next key overrides the previous key.
print(user['age'])
