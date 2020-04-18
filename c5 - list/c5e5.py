# common elements finder function
# define a function which takes 2 lists as input and returns a list which contains common elements of both the lists 

# for example 
# input: [1,2,5,8],[1,2,7,6]
# returns: [1,2]
#### Sol ###############################

def commons_list(l1,l2):
    commn_list = []
    for i in l1:
        if i in l2:
            commn_list.append(i)
    
    return commn_list


l1 = [1,2,5,8]
l2 =[1,2,7,6]

print(commons_list(l1,l2))