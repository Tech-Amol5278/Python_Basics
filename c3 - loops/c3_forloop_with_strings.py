name = "amol"

for i in range(len(name)):
    print(name[i])

print("same can be done using other way")    

for i in name:
    print(i)

### Example : 1256 ----- > 1+2+5+6

num = input("Enter a number to get the sum of its digits: ")

tot_num = 0

for i in num:
    i = int(i)
    tot_num += i
    i += 1
    
print(tot_num)



