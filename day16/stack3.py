list=[0]*5;
top=-1;

while True:
    print("\n1:PUSH");
    print("2:POP");
    print("3:DISPLAY");
    print("4:Exit");
    choice=int(input("Enter your choice\n"));
    
    match choice:
        case 1:
            if top==(len(list)-1):
                print("Stack is overflow");
            else:
                top=top+1;
                value=int(input("Enter value in stack\n"));
                list[top]=value;
                print("Data inserted successfully");
                
        case 2:
            if top==-1:
                print("Stack is underflow");
            else:
                value=list[top];
                top=top-1;
                print("Deleted value is ",value);
                
        case 3:
            if top==-1:
                print("Stack is underflow");
            else:
                i=top;
                while i>=0:
                    print("List = ",end=" ")
                    print(list[i]);
                    i=i-1;
                   
        case 4:
            exit(0);
        case _:
            print("wrong choice");
