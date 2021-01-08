################################################## import all modules ##################################################
import os
import shutil
########################################################################################################################



# get all the files and folders in the current directory
allFiles = os.listdir()


# Loop through all items in the current directory
for item in allFiles:

    # Continously update all the files and folders in the current directory
    allFiles = os.listdir()

    # Check if the item is a file
    if os.path.isfile(item) and item != "FileSorter.py":
        filename, fileExtension = os.path.splitext(item)

        fileExtension = fileExtension[1:]
    
        if fileExtension not in allFiles:
            os.mkdir(fileExtension)
        else:
            pass

        dirPath = os.getcwd()
        shutil.move(dirPath + "\\" + item, dirPath + "\\" + fileExtension + "\\" + item)
    else:
        pass


allFiles = os.listdir()
    
filename, fileExtension = os.path.splitext("FileSorter.py")

fileExtension = fileExtension[1:]
        
if fileExtension not in allFiles:
        os.mkdir(fileExtension)
else:
    pass

dirPath = os.getcwd()
shutil.move(dirPath+"\\"+"FileSorter.py", dirPath+"\\"+fileExtension+"\\"+"FileSorter.py")