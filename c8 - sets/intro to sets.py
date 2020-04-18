# Intro to sets
# Set is data type 
# Set can store - integer, float,string, tuple
# set cannot store list, dictionaries
# Unordered collection of unique data
# returns only unique item
# add method
# remove method 
# discard method
# clear method 
# copy




s = {1,2,3,4,2,3}
print(s)

# Since, it is unordered data type , there is no indexing, we cannot access the data based on the index.
# See below, this returns error

# print(s[1])

## To remove the duplicates from list, for example 
l = [1,22,3,4,6,6,6,6,6,2,2,2,3,4,7,8]
    # convert the list into set
s1 = set(l)
print(s1)
    # convert set to list
s1 = list(s1)
print(s1)
###################################################

# add method - to add the elements 
s.add(89)
print(s)

# remove method - to remove the data/elements 
s.remove(89)
print(s)
# if we try to remove an item which is not available in set from remove method, it gives an error
# s.remove(89)
# print(s)
# Try discard method instead when we dont know the whether item exists 
s.discard(89)
print(s)

# clear method - to empty/clear the set
s.clear()
print(s)

# copy - to make the copy of set
s2 = s1.copy()
print(s2)

# store tuple in sets 
s3 = [1, 2, 3, 4, 6, 7, 8, 22,(1,2,3)]
print(s3)




