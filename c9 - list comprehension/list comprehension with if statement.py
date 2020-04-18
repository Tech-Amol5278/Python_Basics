# list comprehension with if statement

numbers = list(range(1,11))
print(numbers)
 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# to get only odd numbers into another list
#output - [1,3,5..]

    # normal method 
el = []
for i in numbers:
    if i%2 != 0:
        el.append(i)

print(el)

    # with comprehension method 
el2 = []
el2 = [i for i in numbers if i%2 !=0 ]
print(el2)



