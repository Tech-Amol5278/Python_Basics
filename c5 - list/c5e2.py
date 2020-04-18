# define a function which takes list as arguement and this function will return a reversed list 
# try to do this with the help of append and return method

# examples 
# input : [1,2,3,4]
# returns : [4,3,2,1]
# input : ['word1','word2','word3','word4']
# returns : ['word4','word3','word2','word1']

num1 = [1,2,3,4]
words1 = ['word1','word2','word3','word4']
##### Sol1 ########################

def list_reverse1(list1):
    return (list1[::-1])

print(list_reverse1(num1))

##### Sol2 ########################

def list_reverse2(list2):
    rev_list = []
    list2_len = len(list2)
    i = 0
    while i < len(list2):
        list2_len -= 1
        rev_list.append(list2[list2_len])
        i += 1
    return(rev_list) 

print(list_reverse2(words1))


