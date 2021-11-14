import re

openText = open("Text.txt", "r")
readText = openText.read()
openText.close()

Prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
Suffixes = "(Inc|Ltd|Jr|Sr|Co)"
Digits = "([0-9])"
Websites = "[.](com|net|org|io|gov)"
etc = "(i)[.](e)[.]"

editText = readText.replace("\n"," ") # replaces line with space
editText = re.sub(Prefixes,"\\1<prd>",editText) # avoids splitting after prefixes
editText = re.sub(Websites,"<prd>\\1",editText) # avoids splitting between a website
editText = re.sub(" "+Suffixes+"[.]"," \\1<prd>",editText) # avoid splitting after suffix
editText = re.sub("[.]" + Digits,"<prd>\\1",editText) # avoids splitting at a period between 2 numbers
editText = re.sub(Digits + "[.]" + Digits,"\\1<prd>\\2",editText) # avoids splitting at a period between after a number
editText = re.sub(etc, "i<prd>e<prd>", editText)  # converts i.e. to i<prd>e<prd>

# adds a <stop> after sentence boundaries
editText = editText.replace("...","<prd><prd><prd><stop>")
editText = editText.replace(".",".<stop>")
editText = editText.replace("?","?<stop>")
editText = editText.replace("!","!<stop>")
editText = editText.replace("<prd>",".")
splitSentence = editText.split("<stop>")
splitSentence = [sentence.strip() for sentence in splitSentence] # removes leading and trailing spaces

print(*splitSentence, sep="\n") # prints sentences