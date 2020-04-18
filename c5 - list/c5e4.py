# define a function which returns a lists inside list, inner lists are odd and even numbers 
# for example 
# input : [1,2,3,4,5,6,7,8]
# returns : [[1,3,5,7],[2,4,6,8]]

####### Sol ###############################################
num1 = [1,2,3,4,5,6,7,8]

def separate_odd_even(list1):
    sep_list = []
    odd = []
    even = []

    for i in list1:
        if i%2==0 :
            even.append(i)
        else:
            odd.append(i)

    sep_list = [odd,even]
    return(sep_list)

print(separate_odd_even(num1))


