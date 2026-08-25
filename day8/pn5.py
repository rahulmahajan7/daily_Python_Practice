for i in range(65,70):
    count=i
    for j in range(65,75):
        if j<=i : 
            print(chr(j),end=" ")
        elif j>i and count>65 :
            count=count-1
            print(chr(count),end=" ")     
        else:
            print(" ",end=" ")
        
    print()
    
   