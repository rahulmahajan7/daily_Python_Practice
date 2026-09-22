
def getmajority(numbers):
    count=1
    for i in range(len(numbers)-1):         
        for j in range(i+1,len(numbers)):
            if numbers[i]==numbers[j]:
                count=count+1
    if count>len(numbers)//2:
        print("majority of elements are ",numbers[i])
    else:
        print("Majority elemnet not Found")
    return count;
   
plist=[0]*5
i=0
while i<len(plist):
    num=int(input("Enter"+str(i+1)+" numbers "))
    plist[i]=num
    i=i+1
result=getmajority(plist);
