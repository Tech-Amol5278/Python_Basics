# list comprehension with if else 

nums = [1,2,3,4,5,6,7,8,9,10]
# output for odd number multiply by -1 and for even numbers , its square
# [-1,4,-3,16,...]

new_list=[]
    # normal method
for i in nums:
    if i%2 == 0:
        new_list.append(i**2)
    else:
        new_list.append(-i)

print(new_list)

# comprehension method 

new_list2 = [ i**2 if (i%2 == 0)  else -i for i in nums]
print(new_list2)
