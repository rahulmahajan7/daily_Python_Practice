for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==5 or(i>2 and ((i==3 and j<=i)or(j%2==1 and i==4))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()