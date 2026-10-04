s1=set()
s2=set()
i=0 
while i<3:
    value1=int(input("Enter a number for set 1 "))
    s1.add(value1)
    i=i+1
i=0
while i<5:
    value2=int(input("Enter a number for set 2 "))
    s2.add(value2)
    i=i+1
print(s1)
print(s2)
result=(s1<=s2)
if result:
    print("s2 is superset s1")
else:
    print("s2 is not superset of s1")