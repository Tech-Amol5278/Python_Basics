# any and all functions practice

# define a function to return the sum of the values in list

l = [ 1,2,5,7,'Amol']


def mysum(*args):
    sum_val = 0
    if all([type(i) in (int,float) for i in args]):
        for num in args:
            sum_val += num 
    else:
        return 'Please cross check entered values'
    return sum_val

print(mysum(*l))
