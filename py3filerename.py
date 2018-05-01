import os
import re

FILE_PATH="C://Users//cuiyi//Downloads//MA//TEST"
# for i in os.walk(path):
# 	print(i) 
fileLists = []
pattern = re.compile(r'.\d')
def renameFile(path):
    fileList = os.listdir(path)
    for file in fileList:
        newPath = os.path.join(path, file)  
        # print("======="+newPath)
        if os.path.isdir(newPath):
            renameFile(newPath) 
        elif os.path.isfile(newPath):
            filename=os.path.splitext(newPath)[1].upper()
            print(filename)
            match = pattern.match(filename)
            print(match)
            if match:
                print("OLD:====="+newPath)
                fileLists.append(os.path.basename(newPath))
            

renameFile(FILE_PATH)
print(fileLists)