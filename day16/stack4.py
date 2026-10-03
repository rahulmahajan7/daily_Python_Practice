stack=[0]*5;
top=-1;

while True:
    print("1:PUSH");
    print("2:POP");
    print("3:Peek")
    print("4:DISPLAY");
    print("5:Exit");
    choice=int(input("Enter your choice\n"));
    
    match choice:
        case 1:
            if top==(len(stack)-1):
                print("Stack is overflow");
            else:
                top=top+1;
                value=int(input("Enter value in stack\n"));
                stack[top]=value;
                print("Data inserted successfully");
                
        case 2:
            if top==-1:
                print("Stack is underflow");
            else:
                value=stack[top];
                top=top-1;
                print("Deleted value is ",value);
        case 3:
            if top==-1:
                print("Stack is underflow");
            else:
                    print(stack[top]);
                    print("position of top is ",top)       
        case 4:
            if top==-1:
                print("Stack is underflow");
            else:
                i=top;
                while i>=0:
                    print("stack = ",end=" ")
                    print(stack[i]);
                    i=i-1;
                   
        case 5:
            exit(0);
        case _:
            print("wrong choice");
