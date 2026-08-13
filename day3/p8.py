i=1
while i<=5:
    j=1
    while j<=9:
        if j>=6-i and j<=4+i:
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1
    print("")