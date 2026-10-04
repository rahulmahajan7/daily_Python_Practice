s=set()
i=1
while i<=5:
    value=int(input("Enter a number"))
    s.add(value)
    i=i+1
print("Set before remove element",s)
num=int(input("Enter value to remove from set"))
s.remove(num)
print("Set after element is removed",s)