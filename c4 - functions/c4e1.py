# define a function to check which number is greater


## Sol ################################
def big_num(n1,n2):
    if n1 > n2:
        return n1 
    elif n2 > n1:
        return n2
    return "Number Equals"

num1,num2 = input("Enter two numbers, separated by comma: ").split(",")
num1 = int(num1)
num2 = int(num2)
print(big_num(num1,num2))

