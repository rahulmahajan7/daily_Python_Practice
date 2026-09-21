list=[]
n=5
for i in range(n):
    element = int(input("Enter element : "))
    list.append(element)
slarge=-2147483648
large=list[0]
for i in range(len(list)):
    if list[i]>large:
        slarge=large
        large=list[i]
    elif list[i]!=large:
        if list[i]>slarge:
            slarge=list[i]
print(slarge)        