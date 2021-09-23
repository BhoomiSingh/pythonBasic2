import os
import shutil
source= input('enter the soorce folder name')
destination= input('enter the destination name')
source= source+"/"
destination= destination+"/"
listOfFiles= os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)