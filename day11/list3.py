list = [1,2,3,5,6]

list2 = []
for i in range(1,len(list) + 1):
    list2.append(i)
    if list2[i-1] not in list:
        print(i)   