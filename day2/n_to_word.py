#Question 35: Write a Python program to enter a number and print it in words.
num=int(input("Enter number "))
while num>0:
    result=num%10
    num=num//10
    match result:
        case 0:
            print("Zero")
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case 4:
            print("Four")
        case 5:
            print("Five")
        case 6:
            print("Six")
        case 7:
            print("Seven")
        case 8:
            print("Eight")
        case 9:
            print("Nine")
        