def getPalindrome(numbers):
    sum=0
    i=0
    while i<len(numbers):
        if numbers[i]%2==0:
            sum=sum+numbers[i]
        i=i+1
    return sum;
            
    
plist=[0]*6
i=0
while i<len(plist):
    num=int(input("Enter"+str(i+1)+" numbers "))
    plist[i]=num
    i=i+1
    
result=getPalindrome(plist)
print(result)