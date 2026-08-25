for i in range(1,6):
    n=5
    for j in range(1,6):
        if i==1:
            print(j,end=" ")
        elif i>1 and (j==1 or j==6-i):
            if j==1:
                print(i,end=" ")
            else:
                print(n,end=" ");

        else:
            print(" ",end=" ")
    print()