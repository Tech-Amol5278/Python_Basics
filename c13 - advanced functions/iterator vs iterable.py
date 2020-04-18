# Iterators and Iterables

numbers = [5,6,7,8]  ## Iterables, can be lists,tuples,dicts
squares = map(lambda i:i**2, numbers) ## Iterators

# for example 

next_num = iter(numbers)
print(next(next_num))
print(next(next_num))
print(next(next_num))
print(next(next_num))
# print(next(next_num))   ## this returns error because there are no more iterables/items

print(iter(numbers))   ## iterator object

### check for the iterators, no need to iter the they have already been itered , only we can get the next value
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))



