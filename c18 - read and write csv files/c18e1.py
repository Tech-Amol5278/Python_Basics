import pdb
# Excersize

# file-1
# harshit,100
# mohit,50
# aditya,200
# nitish,500

# make another file using file-1:
# Expected output should be :
# harshit's salary is 100
# mohit's salary is 50
# aditya's salary is 200
# nitish's salary is 500


#### Sol 

# pdb.set_trace()
with open('raw_sal.txt') as rs:
    with open('empsal.txt','a') as es:
        for line in rs.readlines():
            name,sal = line.split(",")
            es.write(f"{name}'s salary is {sal}")








