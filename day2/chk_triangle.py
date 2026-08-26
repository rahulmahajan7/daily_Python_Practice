s1=int(input("Enter 1st side of triangle"))
s2=int(input("Enter 2nd Side of triangle"))
s3=int(input("Enter 3rd Side of triangle"))
if s1==s2==s3:
    print("Triangle is equivalent")
elif s1==s2 or s2==s3 or s1==s3 :
    print("triangle is isosceles")
else:
    print("Triangle is scalene")       