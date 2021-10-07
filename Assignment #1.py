
Number = int(input("Enter Number:"))

if(Number % 11 == 0):
    print("a")

if(Number % 9 == 0):
    print("b")

if(Number % 7 == 0):
    print("c")

if(Number % 2 == 0):
    print("d")

if(Number % 11 > 0 and Number % 9 > 0 and Number % 7 > 0 and Number % 2 > 0):
    print("e")