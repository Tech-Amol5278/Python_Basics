# generate lists with range functions 
    # start - optional
    # stop - endpoint of the sequence, this item will not be included in the sequence
    # step - step size of the sequence


numbers = list(range(2,20))
print(numbers)  # range([start,] stop [, step])

# More about POP method 
    # POP removes the lasst element from the list.
    # It also returns the Popped/removed element

# numbers.pop() # this removes the last element
print(numbers.pop())
print(numbers)

# Index - returns the position of string
num2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 8, 15, 16, 17, 18,8,2,5,8]
# check the position of 9
print(num2.index(9))

# Check the position of 1st 8
print(num2.index(8))

# Check the position of 2nd 8
print(num2.index(8,7))   # optional start arguement

# Check the position of 2nd 8
print(num2.index(8,7,15))   # optional stop arguement to search between specific position







