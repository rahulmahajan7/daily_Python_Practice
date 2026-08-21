i=1
while i<=7:
    j=1
    while j<=7:
        if j<=i or j==8-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()
  