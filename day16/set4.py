s=set()
i=0
while i<5:
    value=int(input("Enter a number"))
    s.add(value)
    i=i+1
print(s)
number=int(input("Enter number to search"))    
result=number in s
if result:
    print("Given number is present in Set")
else:
    print("Given number is not present in Set")
