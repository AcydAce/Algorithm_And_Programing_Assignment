

Old_Text = open("Old_Text.txt", "r")
Old_Textline = Old_Text.readlines()  # opens text file
New_Text = open("New_Text.txt", "w")

line = 1  # starting line

for i in Old_Textline:
    New_Text.write(f"{line} "+i)  # insert number into each line
    line += 1

Old_Text.close()
New_Text.close()