import pdb
## To open file

# open() - to open files
# read() - to read the files from python
# tell() - gets the cursor position 
# seek() -  change the posiion of cursor
# readline() - returns a line at a time
# readlines() - returns the output in list format, lines wise

# pdb.set_trace() 
f = open('file1.txt')  ## mode 'r' is deault for reading if not provided.
## to open the files at diffrent location
f = open(r'D:\amol_lap_data\python_tutor\harshit_new\c18\file1.txt')  ## mode 'r' is deault for reading if not provided.



# f.read()    ## this will return the data in string format but to see this we need to print, see below
print(f"cursor position taken before read is at {f.tell()}")

# print(f.read())
# print(f.read())  ### printing or accessing the file multiple files will return output only once, as if it has been executed one time
# print(f"cursor position after read is at {f.tell()}")

# print(f"before seek method, cusrsor at {f.tell()}")
# f.seek(0)
# print( f"after seek method position cusrsor at {f.tell()}")
# print(f.read())

# print(f.readline())
# print(f.readline(), end='')  ## end='' : to remove the line breaks
# print(f.readline())

# lines = f.readlines()
# print(lines)

# lines = f.readlines()[::2]  ## two read only two lines
# print(lines)



# data desscriptors
# name - to get the name of the file
# closed - retursn boolean value if the file is closed or not, see below:

print(f.name)
print(f.closed)





f.close()