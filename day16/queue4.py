# def CheckEmpty(front, rear):
    # if front == -1 and rear == -1:
        # print("Queue is empty")
    # else:
        # print("Queue is not empty")
# queue = [0] * 5
# front = -1
# rear = -1
# i = 0
# while i < 5:
    # value = int(input("Enter value: "))
    # queue[i] = value
    # if front == -1:
        # front = 0
    # rear = rear + 1
    # i = i + 1
# CheckEmpty(front, rear)
# print(queue)
def CheckEmpty(front, rear):
    if front == -1 and rear == -1:
        print("Queue is empty")
    else:
        print("Queue is not empty")


queue = []*5

front = -1
rear = -1

CheckEmpty(front, rear)