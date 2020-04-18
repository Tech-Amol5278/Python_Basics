# exercise one of three
# sum of n natural numbers
# ask a user natural number 
# print total from 1 to n 

############## Sol ##########################################################

n = input("Enter a number: ")
n = int(n)

n_sum = 0
i = 1
while i <= n:
    n_sum += i
    i += 1 

print(n_sum)




