import os
import shutil

folderpath=input("Enter Path: ")
os.chdir(folderpath) # check the path 
os.getcwd() # get the path
os.listdir() # check the files.

# get the extention ans store it in list.
list_extention = []
for f1 in os.listdir():
    extention = f1.split(".")[-1] # break the file name after extantion.
    list_extention.append(extention)
print(list_extention)
list_extention=set(list_extention) # remove duplicate extantion in list

# print extention.
print('Extentions available in Folder:\n',list_extention)

# How to make folder and trnsfer the files in particular extention folder.
for ex in list_extention:
    print(ex,end=",")
    os.mkdir(folderpath + "\\"+ ex) # Make Extantion wise folder.
    for fl in os.listdir():
        if ex in fl:
            shutil.move(fl,folderpath+"\\"+ex) # move file in particular folder. 

else:
    print('\nYour Folder is catorize sucessfully.')