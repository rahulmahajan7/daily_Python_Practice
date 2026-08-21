i=1
while i<=6:
    j=1
    while j<=3:
        if (j<=i and i<=3) or (i>3 and j<=i-3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()