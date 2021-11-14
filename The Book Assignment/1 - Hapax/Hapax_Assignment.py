"""import os
import re
encode = 'utf-8'
import codecs

os.chdir("E:\Bayu's Stuff\Work")
                                                                                                              ----------------------------------------

myFile = open("book.txt""r")
with codecs.open('Book.txt', 'rb', 'utf-8', errors='replace') as f:                                           # Unable to solove UnicodeDecodeError :(
    for line in f:

        fileContents = myFile.read()                                                                          ----------------------------------------
        filecontents = myFile.replace('\\', '/')
        print(fileContents[2])"""


"""--------------------The Code Working as intended------------------------------"""


import re


file = open("Temporary_Book.txt","r")
words = re.findall('\w+', file.read())

for i in range(len(words)):
    words[i] = words[i].lower()         # replaces uppercase to lowercase
key = {key: 0 for key in words}

for word in words:
    key[word] += 1                      # counts how many same words there are
for word in key:
    if key[word] == 1:                  # make sure the word can only appear for a maximum of 1 time
        print (word)

file.close()