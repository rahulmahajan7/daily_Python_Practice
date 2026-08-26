i=1
while i<=5:
    j=1
    while j<=9:
        if j==i or j==10-i or (i==1 and j%2==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()   