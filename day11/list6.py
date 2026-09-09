list1 = [1, 2, 3, 4, 5, 6]
even = []
odd = []
result = []
for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
for i in range(len(even)):
    result.append(even[i])
    result.append(odd[i])
print(result)