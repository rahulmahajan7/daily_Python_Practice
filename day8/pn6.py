for i in range(1,6):
    count=0 
    for j in range(1,10):
        if j<=4+i and j>=6-i and j<5:
            count=count+1
            print(count,end=" ")  
            
        elif j>=6-i and j<=4+i and count>1 :
            count=count-1
            print(count,end=" ")
            
        else:
            print(" ",end=" ")
        
    print()
    
   