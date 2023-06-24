que=[]
def enqueue_element():
    if len(que)==n:
        print("queue is full")
    else:
        element=input("enter element for  queue")
        que.append(element)
        print(que)
def dequeue_element():
    if not que:
        print("queue is empty")
    else:
        e=que.dequeue()
        print(e,"removed")
        print(que)
n=int(input("enter the size of queue"))
while True:
    print("select the operation 1.enqueue 2.dequeue 3.exit")
    choice=int(input("enter ur choice"))
    if choice==1:
        enqueue_element()
    elif choice==2:
        dequeue_element()
    elif choice==2:
        break
    else:
        print("enter the correct choice")
