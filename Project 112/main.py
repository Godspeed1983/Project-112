import os
import shutil

#Source
from_dir="C:/Users/Innoc/Downloads/Project 112/testA"

#Destniation
to_dir="C:/Users/Innoc/Downloads/Project 112/testB"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extenstion = os.path.splitext(file_name)

    if extenstion==" ":
        continue
    if extenstion in  ['.txt','.doc','.docs','.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+'Document_files'
        path3=to_dir+'/'+'Document_files'+'/'+file_name


        if os.path.exists(path2):
            print("Moving"+file_name+"....")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving"+file_name+"....")
            shutil.move(path1,path3)
        