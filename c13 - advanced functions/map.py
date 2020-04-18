# map function

# input
#     [1,2,3,4]
# output
#     [1,4,9,16]

numbers = [1,2,3,4]


# using list comprehension

lc = [i**2 for i in numbers]
print(lc)

# using loops
sq_l = []
def get_sq(l):
    for i in numbers:
        sq_l.append(i**2)
    return sq_l

print(get_sq(numbers))

# using map

map_l = list(map(lambda i:i**2, numbers))
print(map_l)



## 1.to find the length of each element in length using map
names = ['abc', 'abcd', 'abcde', 'adaedad']

lngth = list(map(lambda i:len(i), names))
print(lngth)

## 2. map object iterable, see below 
length = map(len,names)
for i in length:
    print(i)
 ## map object is ieterable only once , hence below will return anything
for j in length:
    print(j)










