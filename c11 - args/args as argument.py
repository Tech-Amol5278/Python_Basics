def multi_func(*args):
    multy_num = 1
    for i in args:
        multy_num *= i
    return multy_num

print(multi_func(2,2,3))

# if we pass the list function will not return value 

nums = [2,2,3]
print(multi_func(nums))   # See this dint work because entire list is bing passed as argument

# to do this with the list, we will have to extract/unpack the list elements 

print(multi_func(*nums))   ## * to unpack the lists i,e args as arguement





