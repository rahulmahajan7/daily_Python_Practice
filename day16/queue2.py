def Front(queue, i):
    if i == 0:
        print(queue[i])
        return
    Front(queue, i - 1)

queue = [10, 20, 30, 40, 50]
Front(queue, 0)