list=[]
n=5
for i in range(n):
    element = int(input("Enter element {i+1}: "))
    list.append(element)
index=int(input("Enter index to insert element"))
value=int(input("Enter value to insert element"))
list.append(0);
i=len(list)-2;
while i>=index:
    list[i+1]=list[i];
    i=i-1;
list[index]=value;
print(list)