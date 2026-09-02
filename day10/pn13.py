n=0
res=1
for i in range(1,9):
    flag= True
    for j in range(1,7):
        if i<=4:
            if j<=i+n and flag:
                print(res,end=" ")
                res=res+1
                flag=False
            else:
                print(" ",end=" ")
                flag=True
        else:
            print("*",end=" ")
    print()
    n=n+1