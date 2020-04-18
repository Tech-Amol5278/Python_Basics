# Define a function which accepts the list and returns the list with 1st letter of the elements in caps 

# input 
#     ["amol",'vishal']
# output
#     ["Amol",'Vishal']
######################

l = ["amol",'vishal']

def Cap(*args):
    al = [i.capitalize() for i in args]

    return al

print(Cap(*l, reverse_str = True))



