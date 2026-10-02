numbers=[0]*5
i=0
while i<len(numbers):
    num=int(input("Enter"+str(i+1)+" numbers "))
    numbers[i]=num
    i=i+1
L=0
R=len(numbers)-1
flag=True
while L<=R:
    
    if numbers[L]!= numbers[R]:
        flag=False   
        break
        
    L=L+1
    R=R-1
    
print(flag)

if flag:
    print("The List is palindrome")
else:
    print("The List is not palindrome")