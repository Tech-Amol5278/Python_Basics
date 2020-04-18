# list comprehension
# with the help of this, we can create a list in one line of code

# create a list of squares from 1 to 10 (traditional method)

sq_l = []
for i in range(1,11):
    sq_l.append(i*i)

print(sq_l)

# create a list of squares from 1 to 10 (compreshension method)

sq_l2 = [i*i for i in range(1,11)]
print(sq_l2)

# List of negative numbers from 1 to 10 (traditional method)
nl = []
for i in range(1,11):
    nl.append(i*-1)
print(nl)    
    
# List of negative numbers from 1 to 10 (comprehension method)

nl2 = [i *(-1) for i in range(1,11)]
print(nl2)

### Ex1 ##
# input - ['Amol','Rahul','Vishal']
# output - ['A','R',"V"]

l = ['Amol','Rahul','Vishal']

    # normal method
ol = []
for ele in l:
    ol.append(ele[0])
print(ol)

    # comprehension method
ol2 = [ele[0] for ele in l]
print(ol2)



    





