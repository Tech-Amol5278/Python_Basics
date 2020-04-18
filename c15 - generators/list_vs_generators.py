# List vs Generators
# memory usage and time consumption
# when to use list, when to user generators 


import time

t1 = time.time()
lc = [i**2 for i in range(1,10000000)]   ## this takes too much unpredictable time
print(f"Time taken using list is {time.time()-t1}")

t2 = time.time()
gc = ( i**2 for i in range(1,10000000) )
print(f"Time taken using generators is {time.time()-t2}")
