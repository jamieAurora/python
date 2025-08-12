from pathlib import Path
import os

dirPath = 'C:\\Users\\byaal\\pythonfiles\\'
myFile = open(dirPath + 'madLibBase.txt')
myData = myFile.read()
myData = myData.split(' ')
print("Enter ADJECTIVE")
noun1 = 'NULL'
adjective = input()
print("Enter NOUN")
noun1 = input()
print("Enter VERB")
verb = input()
print("ENTER SECOND NOUN")
noun2 = input()
noun1checked = 'NULL'
writeData = ''
i = 0
for word in myData:
    #print(word)
    if word == 'ADJECTIVE':
       myData[i] = adjective
       print("We got here")
    if word == 'NOUN':
        if noun1checked == 'NULL':
            myData[i] = noun1
            noun1checked = 'CHECKED'
        else:
            myData[i] = noun2
    if word == 'VERB':
        myData[i] = verb
    if word == 'VERB.':
        myData[i] = verb + '.'
    writeData = writeData + myData[i] + " "
    i = i + 1
    
#print(myData[])
print(myData)
print(writeData)
#myFile.write(writeData)
#myFile.close()
f = open(dirPath + 'madLibFinished.txt', "w")
f.write(writeData)
f.close()
#adjective
#noun
#verb
#noun
