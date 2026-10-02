numbers=[0]*5
i=0
while i<len(numbers):
    num=int(input("Enter"+str(i+1)+" numbers "))
    numbers[i]=num
    i=i+1
n=int(input("Enter an index You want to remove element"))
s=len(numbers)-1
i=len(numbers)-1    
while i>n:
    numbers[i-1]=numbers[i]
    i=i-1
i=0
while i<s: 
    print(numbers[i],end=" ")
    i=i+1