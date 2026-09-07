list=[10,20,30,40,50];

index=int(input("Enter index\n"));
value=int(input("Enter value\n"));
print("List After inserting data");
list.append(0);
i=len(list)-2;
while i>=index:
    list[i+1]=list[i];
    i=i-1;
list[index]=value;
for i in range(len(list)):
    print("list["+str(i)+"]--->"+str(list[i]));
