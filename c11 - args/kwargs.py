# kwargs (keyword arguements)
# **kwargs (double star operator)

# **kwargs as parameter

def kwarg_test(**kwargs):   ## this always store the data in dict datatype/format
    print(kwargs)
    print(type(kwargs))
    return 1

print(kwarg_test(first_name = 'Amol',Last_name = "Chavan"))

## kwargs as arguement / dictionary unpacking 

d = {'fname':'Amol','lname':'Chavan'}
print(d)

# below returns the error,
# print(kwarg_test(d))

# to do this , need to unpack the dict first 
print(kwarg_test(**d))




