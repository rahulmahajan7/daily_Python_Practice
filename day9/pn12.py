'''n = 1
    count = 4

    for i in range(1, 9):
        flag = True

        for j in range(1,i+n):
            if i <5 and flag:
                print(i, end=" ")
                flag = False
            elif i>=5  and flag:
                print(count, end=" ")
                flag = False

            else:
                print("*", end=" ")
                flag = True

        if i >=5:
            count=count - 1
            n=n-2      
        else:
            n = n + 1

        print()'''
for i in range(1, 9):

    if i <= 4:
        count = i
    else:
        count = 9 - i

    for j in range(count):
        print(count, end=" ")

        if j < count - 1:
            print("*", end=" ")

    print()