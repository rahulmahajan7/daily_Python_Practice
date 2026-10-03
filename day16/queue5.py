stack=[0]*5
top=-1
if top==len(stack)-1:
    print("stack is overflow")
else:
         top= top+1
        value=int(input("Enter value in stack\n"));
        stack[top]=value;
        print("Data inserted successfully",value);
        print("position of top is",top)

    