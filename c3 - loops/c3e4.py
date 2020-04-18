# problem
# ask a user to input a number containing more than one digit 
# example - 1256
# calculate 1+2+5+6 and print 

########### Sol ##################################################################################

user_num = input("Enter a number more than one digit to get the sum: ")

len_usernum = int(len(user_num))
sum_num = 0
i = 0

while i < len_usernum:
    sum_num += int(user_num[i])
    i += 1

print(f"sum of your number is {sum_num}")
###################################################################################