# List inside list 

matrix = [[1,2,3],[4,5,6],[7,8,9]]   # this list also called as 2D list


# list (matrix) has only 3 elements 
print(matrix[0])

# printing the elements in the sublists

for sublist in matrix:
    print(sublist)
    for elements in sublist:
        print(elements)

# accessing element 5

print(matrix[1][1])

## to know the data type 
s = 'string'
print(type(s))

print(type(matrix))



