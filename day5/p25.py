i = 1
while i <= 9:
    j = 1
    while j <= 9:
        if j<=6-i or j>=4+i or i>=4+j or j>=14-i and i<=9 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print("")
    i+=1