# How to add data to the list
# append : adds data in list to very last position
# insert : inserts data into the given position
# + : concatenation of strings
# extend : extend the existing string

#### append methods 
fruits = ["grapes","apple"]
fruits.append("mango")
print(fruits)

#### insert method
fruits1 = ["mango","orange"]
fruits1.insert(1,"grapes")
print(fruits1)
#### concatenation of strings
fruits2 = ["guava","banana"]
fruits = fruits1 + fruits2
print(fruits)

#### extend method 
fruity1 = ["mango","orange"]  ## extend in the same list
fruity2 = ["grapes",'apple']
fruity1.extend(fruity2)
print(fruity1)

