#find the maximum differen between given listnumbers = [7, 1, 5, 3, 6, 4]
max1=0
i=0
while i<len(numbers)-1:
    j=i+1
    while j<len(numbers):
        diff=numbers[j]-numbers[i]
        if diff>max1:
            max1=diff
        j=j+1
    i=i+1
print(max1)
