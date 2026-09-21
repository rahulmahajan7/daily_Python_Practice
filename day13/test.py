list =[]
n=6
for n in range (n):
    element=int(input("Enter any number"))
    list.append(element)
target=int(input("Enter number to check frequency"))
count=0
for i in range(len(list)):
        if list[i]==target:
            count=count+1
print(count)            
    