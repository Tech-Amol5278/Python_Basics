# With block    
    # this can be used similar to normal file handeling in python, but this has  below advantage
        # no need to close the file manually after file operations, see example below.
# This also called as context manager


with open('file1.txt') as f:
    print(f.read())

print(f.closed)    # this returns True if the file is closed


