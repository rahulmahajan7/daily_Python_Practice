s=set()
i=1
while i<=5:
    value=int(input("Enter a number"))
    s.add(value)
    i=i+1
print(s)
count=0
for number in s:
    count=count+1
print(count)