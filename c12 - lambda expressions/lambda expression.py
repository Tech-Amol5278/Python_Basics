# lambda expression (anonymous function) - it has no names


def add(a,b):
    return a + b

print(add(4,5))

# same can be written using lambda

add2 = lambda a,b:a+b
print(add2(6,8))

# lambda expressions mostly used to work with built-in functions like map,reduce,filter etc..


print(add)   ## <function add at 0x000001968AF53EE8>
print(add2)  ## <function <lambda> at 0x000001968AF53F78>, see this has no name it is unlike add



