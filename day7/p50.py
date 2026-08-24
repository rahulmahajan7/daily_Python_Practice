for i in range(1,6):
    n=1
    flag=True   
    for j in range(1,10):
        if (j==6-i or j==4+i) and i<=4 :
            print(n,end=" ")
            n=i
        elif i==5 and flag :
                print(n,end=" ")
                n=n+1
                flag=False
        else:
            print(" ",end=" ")
            flag=True
    print()