phoneBook={}
n=5
i=0
while i<n:
    name=input("Enter a name")
    number=int(input("Enter a persons number"))
    phoneBook[name]=number
    i+=1
print(phoneBook)