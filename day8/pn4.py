for i in range(1,6):
    count=i
    for j in range(1,10):
        if j<=i : 
            print(j,end=" ")
        elif j>i and count>1 :
            count=count-1
            print(count,end=" ")     
        else:
            print(" ",end=" ")
        
    print()
    
   