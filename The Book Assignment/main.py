import os
import re
encode = 'utf-8'
import codecs

os.chdir("E:\Bayu's Stuff\Work")

myFile = open("book.txt""r")
with codecs.open('Book.txt', 'rb', 'utf-8', errors='replace') as f:
    for line in f:

        fileContents = myFile.read()
        filecontents = myFile.replace('\\', '/')
        print(fileContents[2])


"""--------------------The Code Working as intended------------------------------"""

"""import os
import re

os.chdir("E:\Bayu's Stuff\Work")

file = open("Temporary_Book.txt","r")
words = re.findall('\w+', file.read().lower())
key = {key: 0 for key in words}
for word in words:
    key[word] += 1
for word in key:
    if key[word] == 1:
        print (word)

file.close()"""