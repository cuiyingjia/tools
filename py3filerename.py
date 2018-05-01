import os
path="C://Users//cuiyi//Downloads//MA//TEST"
# for i in os.walk(path):
# 	print(i) 
fileLists = []
def myTotalSize(path):
    memory = 0
    fileList = os.listdir(path)
    for file in fileList:
        newPath = os.path.join(path, file)  
        # print("======="+newPath)
        if os.path.isdir(newPath):
            memory += myTotalSize(newPath) 
        elif os.path.isfile(newPath):
            if os.path.splitext(newPath)[1].upper() == '.LOG':
                fileLists.append(os.path.basename(newPath))
            memory += os.path.getsize(newPath)
    return memory

print(myTotalSize(path))
print(fileLists)
