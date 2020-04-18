# define a function which takes list as arguement and returns list with reverse of every element in that list 

# example 
# input : ['abc','tuv','xyz']
# returns  : ['cba','vut','zyx']
########## Sol ##########################

l = ['abc','tuv','xyz']
ol = [ i[::-1] for i in l]
print(ol)

