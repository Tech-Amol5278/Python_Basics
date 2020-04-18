# in keyword in sets and for loop
# union ( | ) -- pipe operator
# intersection  ( & ) -- and operator

s = {'a','b','c'}

# in keyword to check item is present

if 'a' in s:
    print('present')
else:
    print('not present')

# for loop

for i in s:
    print(i)

#############################################
s1 = {1,2,3,4}
s2 = {3,4,5,6}

# union -- returns all items excluding duplicates
us = s1 | s2 
print(us)

# intersection -- returns only common items
inter_s = s1 & s2
print(inter_s)


