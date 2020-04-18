# pass functions as arguements 

def square(a):
    return a**2

l = [1,2,3,4]
sq_func = map(square, l)
sq_lam = map(lambda i:i**2, l)

print(list(sq_func))
print(list(sq_lam))

## We can also create a function similar as map .i.e a function which can be used instead as map


def my_map(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

sq_lam2 = list(my_map(lambda i:i**2, l))
print(sq_lam2)
















