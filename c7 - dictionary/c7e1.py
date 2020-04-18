# define a function that takes the number (n)  and return a dictionary containing cube of numbers 
# from 1 to n 

# example
# cude finder(3)
# ouput {1:1,2:8,3:27}
########################## Sol ###################################################################

def cube_finder(n):
    
    cube_dict = {}
    i = 1

    while i <= n:
        cube_dict[i] = i**3
        i += 1
    
    return cube_dict


print(cube_finder(4))   


