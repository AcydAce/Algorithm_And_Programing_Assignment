
Number = int(input("Enter Number:"))

if(Number % 11 == 0):
    print("a",end="")

if(Number % 9 == 0):
    print("b",end="")

if(Number % 7 == 0):
    print("c",end="")

if(Number % 2 == 0):
    print("d",end="")

if(Number % 11 > 0 and Number % 9 > 0 and Number % 7 > 0 and Number % 2 > 0):
    print("e")