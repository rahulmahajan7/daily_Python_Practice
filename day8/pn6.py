for i in range(1,6):
    count=1
    for j in range(1,10):
        if j>=6-i and j<=4+i :
            print(count,end=" ")  
            count=count+1
        elif j<=4+i and j>=6-i and count>1:
            print(count,end=" ")  
            count=count-1
        else:
            print(" ",end=" ")
        
    print()
    
   