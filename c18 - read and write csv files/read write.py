# Read and Write 
# Example: creating a new file using existing file'


with open('file1.txt') as r:
    with open('new_file1.txt','w') as f:
        f.write(r.read())

