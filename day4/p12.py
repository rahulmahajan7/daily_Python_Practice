i=1
while i<=5:
    j=1
    while j<=5:
        if j>=i:
            if i%2==1:
                print("#",end=" ")
            else:
                print("*",end=" ")
        j=j+1
    i=i+1
    print("")