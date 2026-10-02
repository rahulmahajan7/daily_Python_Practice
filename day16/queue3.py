def Rear(queue, i):
    if i == 4:
        print(queue[i])
        return
    Rear(queue,i+1)
queue = [10, 20, 30, 40, 50]
Rear(queue, 0)