# To write into files
    # w : This creates the new file or overwrites the existing file with new string given, This can be used when the file is empty or intentionallly
        # we have to overwrite data in file
    # a :  Creates new file or Appends the existing file with given string
    # r+ : This does not creates new file. This will only appends the given string and 
    #   replace the contents of the file with cursor starting from position 0. 


with open("testwrite_w.txt", 'w') as f:
    f.write('Hello')


with open("testwrite_w.txt", 'a') as f:
    f.write('\nwe are  learning file operations in python')


with open("testwrite_w.txt", 'r+') as f:
    f.write('Lets do it')




