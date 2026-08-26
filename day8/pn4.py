for i in range(1,6):
    count=i
    n=0
    for j in range(1,10):
        if j<=i+n  : 
            print(i,end=" ")
            n=n+1
        elif j>i and count>1 :
            count=count-1
            print(count,end=" ")     
        else:
            print(" ",end=" ")
        
    print()
    
   