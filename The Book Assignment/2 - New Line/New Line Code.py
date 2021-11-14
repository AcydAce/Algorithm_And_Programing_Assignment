

Old_Text = open("Old_Text.txt", "r")
oldContent = Old_Text.readlines()
New_Text = open("New_Text.txt", "w")

line = 1

for i in Old_Text:
    New_Text.write(f"{line} "+i)
    i += 1

Old_Text.close()
New_Text.close()