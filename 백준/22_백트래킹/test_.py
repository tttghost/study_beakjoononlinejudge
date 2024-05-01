import os

folderPath=os.path.dirname(os.path.realpath(__file__))
filePath=folderPath+'/test.txt'

result=[]
with open(filePath) as file:
    result=file.readlines()
print('a')
line=0
print(result)
def readline():
    global line
    data=result[line].rstrip()
    line+=1
    return data

