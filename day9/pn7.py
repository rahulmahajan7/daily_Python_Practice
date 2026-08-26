for i in range (1,6):
    flag=True
    for j in range(1,18):
        if j<=8+i and j>=10-i and flag:
            print(i,end=" ")
            flag=False
        else:
            print("*",end=" ")
            flag=True
    print()