def getPalindrome(numbers):
    i=len(numbers)-1
    nlist=[]
    while i>=0 :
        nlist= nlist+ [numbers[i]]
        i=i-1       
    if nlist==numbers:
        print("palindrome")
    else:
        print("Not")
    return nlist;
    
plist=[0]*5
i=0
while i<len(plist):
    num=int(input("Enter"+str(i+1)+" numbers "))
    plist[i]=num
    i=i+1
    
result=getPalindrome(plist)
print(result)