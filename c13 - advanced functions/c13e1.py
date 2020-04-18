# Define a function 
# take any no of lists containing number
# [1,2,3],[4,5,6],[7,8,9,1]

# returns the average
# [2,5,8.3]
# note : try using lambda
############## Sol using normal method #######################
# nums = [ [1,2,3],[4,5,6],[7,8,9,1] ]
# # nums = [ [1,2,3] ]
# avg = []
# # normal method to get the average of elements in sublist

# def get_avg(*l):
#     for i in l:
#         print(i)
#         sm = 0
#         for j in i:
#             print(f"loop for {j}")
#             sm += j
#             print(sm)
#         avg.append(sm/(len(i)) )
#     return avg

# print(get_avg(*nums))

############## Sol using lambda expression #######################




### get the average of 1st, 2nd and 3rd elements of the sublists

num1 =   [1,2,3],[4,5,6],[7,8,9] 

avg_list = []
def avg_finder(*args):
    for pair in zip(*args):
        avg_list.append(sum(pair)/len(pair))
    return avg_list

# print(avg_finder([1,2,3],[4,5,6]))
print(avg_finder(*num1))

### get the average of 1st, 2nd and 3rd elements of the sublists with lambda

avg_finder2 = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(avg_finder2(*num1))




