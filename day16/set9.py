s=set()
i=1
while i<=5:
    value=int(input("Enter a number "))
    s.add(value)
    i=i+1
print(s)
maxValue=0
minValue=None
for i in s:
    if maxValue<i:
        maxValue=i
    elif minValue is None or minValue>i:
        minValue=i
print(maxValue)
print(minValue)