# define a generator function
# take one number argument
# generate a sequence of even numbers from 1 to that number

# using generator comprehension
def even_num(n):
    gen_evens = (i for i in range(1,n+1) if i % 2 == 0 )  ## use () for gen. comprehension
    return gen_evens


# get_evens = even_num
for i in even_num(8):
    print(i)



def even_gnrt(n):
    for item in range(1,n+1):
        if item%2==0:
            yield(item)

for i in even_gnrt(10):
    print(i)




