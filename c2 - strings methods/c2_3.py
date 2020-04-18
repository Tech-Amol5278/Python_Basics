#### Tut: 34 #################################
# replace method 
# find method 


string =  "She is beautiful and she is a good dancer"

print(string.replace(" ","_"))

print(string.replace("is","was"))
print("see the diffrence")
print(string.replace("is","was",1))
print("now same as ")
print(string.replace("is","was",2))

## find method .. gives position

print(string.find("is"))

###  find secons occurance 

is_pos1 = string.find("is")  ## 1st is

print(string.find("is",is_pos1+1))
