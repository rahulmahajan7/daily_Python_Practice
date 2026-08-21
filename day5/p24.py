i = 1
while i <= 9:
    j = 1
    while j <= 9:
        if j == 6-i or j==4+i or j==5 or i==5 or i>=6 and j==14-i or i==4+j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1