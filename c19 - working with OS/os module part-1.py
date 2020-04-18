# Os module part-1
# This module lets you work with operating system

import os ## importing os module

# to get the current working directory
print(os.getcwd())

# to create a folder in current working directory
# os.mkdir('new_dir')

# to check if the directory alteady exists
print(os.path.exists('new_dir'))

# open a file if it is not exist without any error.
open('file_open.txt','a').close()

# to change directory
os.chdir(r'D:\amol_lap_data\python_tutor\harshit_new')
print(os.getcwd())

# to know the files/folders available in directory
print(os.listdir())

# To join the paths
# syntax: os.path.join(r'',file_name)


