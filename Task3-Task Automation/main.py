import os
import shutil

path=input("Enter the path: ")
files=os.listdir(path)

for f in files:
    filename,extension=os.path.splitext(f)
    extension=extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+f,path+'/'+extension+'/'+f)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+f,path+'/'+extension+'/'+f)