# filter function

# to check the number is even 

def is_even(a):
    return a%2 == 0

numbers = [3,4,2,1,5,6,9,8,10]

## filter only the even numbers from numbers list

evens = tuple(filter(is_even, numbers))
print(evens)

# we can also use lambda
evens = tuple(filter(lambda i:i%2==0 , numbers))
print(evens)


# this is iterable and can be used multiple times unlike map

for i in evens:
    print(i)

for j in evens:
    print(j)
    