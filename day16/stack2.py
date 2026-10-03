stack = [10, 20, 30, 40, 50]
top = 4
if top==-1:
    print("Stack is underflow")
else:
    value=stack[top]
    top=top-1
    print("Deleted value is ",value)
    print("top position is",top)