fruits = ['grapes','mango','apple']   # sort on list

# print(fruits)
# fruits.sort()
# print(fruits)

fruits2 = ('grapes','mango','apple')  #cannot use sort on tuples, returns error. Hence sorted can be used

# print(fruits2)
# fruits2.sort()
# print(fruits2)

print(fruits2)
print(sorted(fruits2))  # sorted - returns output in list


# Same is with the sets (Cannot use sort, only sorted is allowed)
fruits3 = {'grapes','mango','apple'}

# print(fruits3s)
# fruits3.sort()
# print(fruits3)

print(fruits3)
print(sorted(fruits3))  # sorted - returns output in list

#########################
guitars = [
    {'model':'yamaha f310','price': 8400},
    {'model':'faith naptune','price': 50000},
    {'model':'faith apollo venus','price': 35000},
    {'model':'tailor 814ce','price': 450000},
]

# sort the guitars according to prices in ascending order.
# ascending
print(sorted(guitars, key = lambda items: items.get('price') ))
# descending
print(sorted(guitars, key = lambda items: items.get('price'), reverse= True ))











