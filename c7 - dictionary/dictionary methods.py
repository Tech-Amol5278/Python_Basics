# fromkeys method
# get method
# copy method
# clear method 


# fromkeys method

# easier way to assign same/default value to multiple keys

# for example 
# expected output :
# d = {'name':'unknown','age':'unknown'}

d = dict.fromkeys(['name','age'],'unknown')
print(d)

# This will assign two values to each key
d = dict.fromkeys(['name','age'],['unknown',28])
print(d)

# get method
d={'name':'unknown','age':'unknown'}

# Below will return error, since key 'names' not available in dict d
    # print(d['names'])

# To handle such excepions, get method is useful. See below

print(d.get('names'))  ## This returns "None" if key not present


# copy method - to copy dictionary

d1 = d  # this is not copying, this is assigning
d.popitem() 
print(d1) # see this, this is affecting in d1. Since d and d1 are same

d2 = d.copy()  # this is not copying, this is assigning 
print(d1) # copying dictionary

# clear method- to clear/empty dictionary

d.clear()
print(d)


