

AWL = 0   # Average Word Length
SWTL = 0  # Sum Of Word Token Length
NWT = 0   # Number Of Word Tokens

book = open("Temporary_Book.txt", "r")
content = book.read()  # opens file

splitWords = content.split()  # splits words into a list

SWTL = sum(len(word) for word in content.split())
NWT = len(content.split())  # calculates the number of words
AWL = SWTL / NWT            # Average Word Length = Sum Of Word Token Length / Number Of Word Tokens

print("Average Word Length %.3f: " % AWL )
print("Sum of All Lengths of Word Tokens: " , SWTL)  # prints all
print("Number of Word Tokens: " , NWT)