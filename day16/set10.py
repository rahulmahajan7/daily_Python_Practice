s=set()
i=1
while i<=5:
    value=int(input("Enter a number "))
    s.add(value)
    i=i+1
print(s)
odd=0
even=0
for i in s:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)