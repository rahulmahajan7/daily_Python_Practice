l1 = [1, 2, 3]
l2 = [1, 3, 4, 5]

l3 = [0] * (len(l1) + len(l2))
k = 0

for i in range(len(l1)):
    if l1[i] not in l3:
        l3[k] = l1[i]
        k = k + 1

for i in range(len(l2)):
    if l2[i] not in l3:
        l3[k] = l2[i]
        k = k + 1

l3 = l3[:k]

print(l3)