# l1 = [1,2,3,4]
# l2 = [2,4,6,8]

l = [(1,2),(2,4),(3,6),(4,8)]

# get the two lists l1,l2 from l

#  * operator
print(list(zip(*l)))
l1,l2 = list(zip(*l))
print(l1)
print(l2)

# get the max number of pair from lists l1 and l2

l3 = [1,3,5,7]
l4 = [2,2,9,4]

max_nums=[]
for pair in zip(l3,l4):
    max_nums.append(max(pair))
print(max_nums)







