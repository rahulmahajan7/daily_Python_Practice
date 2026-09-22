numbers = [1, 2, 3, 4, 5]
k=int(input("Enter a number"))
for i in range(k):
    last=numbers[len(numbers)-1]
    i=len(numbers)-1
    while i>0:
        numbers[i]=numbers[i-1]
        i=i-1
    numbers[0]=last
print(numbers)