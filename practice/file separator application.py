# File separator application

# Consider a directory which has multiple files such as music,video,doc,excel etc, separate them into diffrent directories
# extension wise

import os,shutil

music_exts = ('.mp3','.aac','.wav','.flac')
vdo_exts = ('.mp4','.flv','.mkv','.3gp')
doc_exts = ('.doc','.txt','.xls','.xlsx','.pdf','.csv')
img_exts = ('.jpg','jpeg','.gif')

search_dir = r'D:\amol_lap_data\python_tutor\practice\raw_dir'
sorted_dir = r'D:\amol_lap_data\python_tutor\practice\sorted_dir'
dirs = ('videos','docs','images','music')

## check and create directory if not exists
for dir in dirs:
    if os.path.exists(os.path.join(sorted_dir,dir)):
        pass
    else:
        os.mkdir(os.path.join(sorted_dir,dir))

m_dir = os.path.join(sorted_dir,'music')
v_dir = os.path.join(sorted_dir,'videos')
d_dir = os.path.join(sorted_dir,'docs')
i_dir = os.path.join(sorted_dir,'images')

## 
os.chdir(search_dir)
# name = '02105160103-06-Apr-2020.pdf'
# print(name)
# print(name[name.find('.'):len(name)])

for file in os.listdir():
    if file[file.find('.'):len(file)].lower() in music_exts:
        os.path.exists(shutil.move(file,m_dir))
    elif file[file.find('.'):len(file)].lower() in vdo_exts:
        os.path.exists(shutil.move(file,v_dir))
    elif file[file.find('.'):len(file)].lower() in img_exts:
        os.path.exists(shutil.move(file,i_dir))
    elif file[file.find('.'):len(file)].lower() in doc_exts:
        os.path.exists(shutil.move(file,d_dir))
    else:
        pass














