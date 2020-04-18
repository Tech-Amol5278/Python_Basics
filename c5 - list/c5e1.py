# define a function which takes list containing numbers as input and return list containing square of every elements

# example 
# input nums = [1,2,3,4]
# returns square_nums = [1,4,9,16]

### Sol ################
def list_square(nums_list):
    sq_list = []
    for i in nums_list:
        sq_list.append(i*i)
    return sq_list


nums = [1,2,3,42,56,22,534,33]
print(list_square(nums))
