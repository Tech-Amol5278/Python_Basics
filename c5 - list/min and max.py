# min and max functions

numbers  = [6,50,2]

print(min(numbers))
print(max(numbers))

# function to get the greatest diffence between the numbers inside the list


def get_diff(l1):
    return(max(l1)-min(l1))

print(get_diff(numbers))