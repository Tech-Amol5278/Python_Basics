# OS module part 2
# to get the folder-subfolders and files from given directory
import os
import shutil
x_dir = os.walk(r'D:\amol_lap_data\python_tutor')

for current_path,folder_names,file_names in x_dir:
    print(f'current path: {current_path}')
    print(f'folder name: {folder_names}')
    print(f'file name: {file_names}')

## to create directory in working directory
print(os.getcwd())
os.makedirs(r'movies\movie-1')


# to delete the directory
# os.rmdir('songs')       # Deletion only happens only if the directory is empty

# to remove the directory tree
shutil.rmtree('movies')

# to copy the tree
shutil.copytree('','')

# to copy files
shutil.copy('','')

# to move a file or folder
shutil.move('','')



