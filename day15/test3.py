numbers=[0]*6
i=0
while i<len(numbers):
    num=int(input("Enter"+str(i+1)+" numbers "))
    numbers[i]=num
    i=i+1
target=int(input("Enter a number to search "))
  
for i in range(len(numbers)):
    if numbers[0]>target:
        Rindex=0
        break 
    elif numbers[len(numbers)-1]<target:
        Rindex=len(numbers)
        break
    elif numbers[i]<=target:
        Lindex=i   
        Rindex=Lindex+1 
    
print(Rindex)        
numbers.append(0)
i=len(numbers)-2
while i>=Rindex:
    numbers[i+1]=numbers[i]
    i=i-1
numbers[Rindex]=target
print(numbers)
    


    

