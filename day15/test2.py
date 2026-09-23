def getPalindrome(numbers):
    L=0
    R=len(numbers)-1
    target=int(input("Enter a number to search "))
    
    while L<R:
        mid=L+(R-L)//2
        print(mid)
        if numbers[mid]==target:
            print("Number found",numbers[mid])
            break
        elif numbers[mid]>target:
            R=mid-1
        else:
            L=mid+1    
    else:
        print("Number Not Found")
    return numbers[mid];
         
plist=[0]*5
i=0
while i<len(plist):
    num=int(input("Enter"+str(i+1)+" numbers "))
    plist[i]=num
    i=i+1
    
result=getPalindrome(plist)
