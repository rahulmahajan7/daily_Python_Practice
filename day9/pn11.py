n=3
count=4   
for i in range (1,8):
    for j in range(1,5):
        if j<=i and i<4:
            print(n,end=" ")
        elif j<=count and i>=4:
            print(n,end=" ")    
        else:
            print(" ",end=" ")
    print()
    if i<4:
        n=n+1
    else:
        count=count-1
        n=n-1
     
    