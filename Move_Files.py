import os
import shutil

from_folder = "Downloads"
to_folder = "C:\Users\Shloa\Desktop\Document_Files"

list_of_files = os.listdir(from_folder)


for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension =='':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1  = from_folder + '/' + file_name
        path2 = to_folder + '/' + "Document_Files"
        path3 = to_folder + '/' + "Document_Files" +file_name

        if os.path.exists(path2):
            print("Moving" + file_name + "......")

            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving"+file_name+"......")
            shutil.move(path1,path3)