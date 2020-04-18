# Common methods to delete data from list
# pop method : to delete if the position is known
# del operator: to delete if the position is known
# remove method: if the postion is unkown but element is known
fruits = ['orange','apple','pear','banana','kiwi']
## pop method
# to element last element  i.e kiwi
fruits.pop()
print(fruits)
# to delete 2nd element i.e apple
fruits = ['orange','apple','pear','banana','kiwi']
fruits.pop(1)
print(fruits)
# del operator
fruits = ['orange','apple','pear','banana','kiwi']
del fruits[1]
print(fruits)
# remove method1, if we knows the element
# it deletes only 1st matching element 
# returns error if element doesnt exist
fruits = ['orange','apple','pear','banana','kiwi']
fruits.remove("apple")
print(fruits)

