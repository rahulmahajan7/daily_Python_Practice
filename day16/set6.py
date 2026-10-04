s1=set()
s2=set()
i=1
while i<=3:
    value1=int(input("Enter a number for set 1 "))
    value2=int(input("Enter a number for set 2 "))
    s1.add(value1)
    s2.add(value2)
    i=i+1
print(s1)
print(s2)
c= s1|s2
print("Union of set s1 and s2",c)