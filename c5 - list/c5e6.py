# define a function which takes list as input and returns the no. of lists inside the input list 

# for example 
# input: [1,2,3,[1,2],[3,4]]
# returns: 2 ## which is count of lists inside the list 
###### Sol #########################################

num_list = [1,2,3,[1,2],[3,4]]

# print(type(l1) is list )

def inner_list_count(l1):
    comm_count=0
    for i in l1:
        if type(i) is list:
            comm_count += 1

    return(comm_count)


print(inner_list_count(num_list))