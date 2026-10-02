def GetQ(Qlist, i):
    if i == 5:
        return

    value = int(input("Enter the value: "))
    Qlist[i] = value

    GetQ(Qlist, i + 1)


Qlist = [0] * 5

GetQ(Qlist, 0)

print(Qlist)