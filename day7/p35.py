for i in range(1,12):
    for j in range(1,10):
        if ((j>=6-i and j<=4+i)and i<=5)or((i>5)and j>=4 and j<=6):
            print("*",end=" ")   
        else:
            print(" ",end=" ")
    print()