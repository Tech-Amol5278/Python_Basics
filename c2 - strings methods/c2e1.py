# ask user to input 3 numbers and you have to print average of three numbers using string formatting.
# bonus: try to take all thhree comma separed inoputs in one line
########## Sol 1 ################
num1  = int(input("Enter 1st no: "))
num2  = int(input("Enter 2nd no: "))
num3  = int(input("Enter 3rd no: "))

tot = (num1+num2+num3)/3
print(tot)
######## Sol bonus #######################

n1,n2,n3 = input("Enter three numbers in comma separated: ").split(",")

tot = (int(n1)+int(n2)+int(n3))/3
print(tot)


