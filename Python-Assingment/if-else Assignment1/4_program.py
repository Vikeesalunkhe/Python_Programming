# program 4: write a python program that checks a no from 0 to 5 and print its spelling if the no. is greaterthan 5 print the no. is graterthan 5


num = int(input("Enter your number :"))

if num == 0:
    print("Zero")
elif num == 1:
    print("One")

elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")

elif num == 5:
    print("Five")

elif num > 5:
    print("number is greterthan 5 ")
else:
    print("invalid number")
