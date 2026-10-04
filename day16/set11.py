list=[]
n=6
i=0
while i<n:
    value=int(input("Enter a number"))
    list.append(value)
    i=i+1
print("List before remove duplicates",list)
s=set(list)
print("List after remove duplicates",s)