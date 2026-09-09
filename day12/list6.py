list=[12,35,1,10,34,2]
max=list[0]
for i in range(len(list)):
    if list[i]>max:
        max=list[i]
print(max)
smax=list[0]
for i in range (len(list)):
    if list[i]>smax and list[i]<max:
        smax=list[i]
print(smax)