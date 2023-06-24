stc=[]
def push_element():
    if len(stc)==n:
        print("stack is full")
    else:
        element=input("enter element for stack")
        stc.append(element)
        print(stc)
def pop_element():
    if not stc:
        print("stack is empty")
    else:
        e=stc.pop()
        print(e,"removed")
        print(stc)
n=int(input("enter the size of stack"))
while True:
    print("select the operation 1.push 2.pop 3.exit")
    choice=int(input("enter ur choice"))
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==2:
        break
    else:
        print("enter the correct choice")