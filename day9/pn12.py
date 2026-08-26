n=0
for i in range (1,9):
    flag=True
    for j in range(1,7):
        if i<=4:
            if j<=i+n and flag:
                print(i,end=" ")
                flag=False
            elif flag==False:
                print("*",end=" ")
                flag=True
            else:
                print(" ",end=" ")
            n=n+1    
        elif i>4:
            n=n-1
            if j>=n and flag:
                print(n,end=" ")
                flag=False
            elif flag==False:
                print("*",end=" ")
                flag=True
            else:
                print(" ",end=" ")
    print()
    
     
    