i=1
while i<=9:
    j=1
    while j<=5:
        if i==1 or j==1 or j==8-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()