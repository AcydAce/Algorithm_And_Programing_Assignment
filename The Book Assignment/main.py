import os
import re
os.chdir("E:\Bayu's Stuff\Work")

myFile = open("Book.txt","r")
fileContents = myFile.read()
print(fileContents[2])

"""def hapax():
    file = open("Book.txt","r")
    words = re.findall('\w+', file.read().lower())
    freqs = {key: 0 for key in words}
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print (word)

"""

file.close()