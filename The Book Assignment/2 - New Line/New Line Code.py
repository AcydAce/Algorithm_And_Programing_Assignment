

Old_Text = open("Old_Text.txt", "r")
oldContent = Old_Text.readlines()
New_Text = open("New_Text.txt", "w")

i = 1

for line in Old_Text:
    New_Text.write(f"{i} "+line)
    i += 1


Old_Text.close()
New_Text.close()