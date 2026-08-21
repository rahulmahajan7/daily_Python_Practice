i=1
while i<=5:
    j=1
    while j<=5:
        if j==6-i or j==1 or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()
    