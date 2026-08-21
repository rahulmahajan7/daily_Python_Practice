i=1
while i<=5:
    j=1
    while j<=9:
        if j==6-i or j== 4+i or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()