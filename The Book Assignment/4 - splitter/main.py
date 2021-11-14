#A pair of list to convert special exceptions from and to back and forth
Titles = ["Mr.", "Mrs.", "Dr.","Jr."]
ReplaceTitles = ["Mister", "Missus", "Doctor","JR"]
Internal = ["e.g.", "i.e."]
ReplaceInternal = ["EG", "IE"]

Text = input("Enter a short text: ")

for x in Titles: #Replaces titles with another name to prevent periods replacement
     i = Titles.index(x)
     Text = Text.replace(x, ReplaceTitles[i])
for x in Internal: #Replaces periods internal with another name to prevent periods replacement
     i = Internal.index(x)
     Text = Text.replace(x, ReplaceTitles[i])

Text = Text.replace(". ", ".\n") #Replaces period with a period and new line
Text = Text.replace("? ", "?\n") #Replaces question mark with a question mark and new line
Text = Text.replace("! ", "!\n")  #Replaces exclamation mark with an exclamation mark and new line

for x in ReplaceTitles: #Reverts  new title name back to old name
    i = ReplaceTitles.index(x)
    Text = Text.replace(x, ReplaceTitles[i])
for x in ReplaceInternal: #Reverts new internal name back to old name
    i = ReplaceInternal.index(x)
    Text = Text.replace(x, Internal[i])

file = open("result.txt", "w")
file.write(Text) #Write the modified short text
file.close()