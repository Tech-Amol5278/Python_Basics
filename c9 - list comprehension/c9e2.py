# Extract only numeric items and convert them into string and make separete list for them
# input ['True','False',[1,2,3],1,1.0,3]
# output ['1','1.0','3']
#### Sol ################

# print(type(1))
# print(type(1.0))

raw_list = ['True','False',[1,2,3],1,1.0,3]

num_list = []
    # normal method
for i in raw_list:
    if type(i) == int or type(i) == float :
        num_list.append(str(i))

print(num_list)

    # comprehension

num_list2 = [str(i) for i in raw_list if type(i) in (int,float)]  # used "IN"
print(num_list2)




