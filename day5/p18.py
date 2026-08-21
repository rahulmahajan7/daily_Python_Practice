i=1
while i<=6:
    j=1
    flag=True
    while j<=11:
        if j>=i and j<=12-i and flag:
            print("*",end=" ")
            flag=False
        else:
            print(" ",end=" ")
            flag=True
        j=j+1
    i=i+1
    print()