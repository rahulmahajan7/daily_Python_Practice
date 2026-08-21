i=1
while i<=9:
    j=1
    flag=True
    while j<=9:
        if ((j>=6-i and j<=4+i and i<=5) or (j<=14-i and i<=4+j and i>5)) and flag  :
            print("*",end=" ")
            flag=False
        else:
            print(" ",end=" ")
            flag=True
        j=j+1
    i=i+1
    print()