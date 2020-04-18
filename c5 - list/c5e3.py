# define a function which takes list as arguement and returns list with reverse of every element in that list 

# example 
# input : ['abc','tuv','xyz']
# returns  : ['cba','vut','zyx']
########## Sol ##########################
words1 = ['abc','tuv','xyz']

def element_reverse(list1):
    rev_ele = []
    for i in list1:
        rev_ele.append(i[::-1])
    return rev_ele

print(element_reverse(words1))




