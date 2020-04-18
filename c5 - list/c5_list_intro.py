# Data Structures
# List
# List is ordered collection of items
# We can store anything in lits like int, float, string

numbers = [1,2,3,4]
print(numbers)
## to print 2 from list 
print(numbers[1])
## to access only and 1 and 2
print(numbers[:2])
## to reverse the elements in list
print(numbers[::-1])
## to access only last element i.e 4
print(numbers[-1])
words = ["word1",'word2','word3']
print(words)

mixed = [1,2,3,4,"five","six",None]
print(mixed)
## to update the elements in list such as 2 > "two"
mixed[1]  = "two"
print(mixed)

mixed[1:]  = "two"  ## considered new list t , w, o
print(mixed)

mixed[1:]  = ["three","four"]
print(mixed)
