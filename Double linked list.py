class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("doublly linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<--->",end=" ")
                temp = temp.next
    def insert_begining(self,data):
        new_node=Node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
        temp.next=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def delete_pos(self,pos):
        temp1=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            temp1=temp1.next
        temp1.next=temp.next
node_1=Node("lakmi")
node_2=Node("jannu")
node_3=Node("ruthwik")
node_4=Node("praneeth")
node_5=Node("lakmarajpalley")
print(node_1.data)
print(node_2.data)
print(node_3.data)
print(node_4.data)
print(node_5.data)
d1=DLL()
d1.head=node_1
print(d1.head)
node_1.prev=None
print(node_1.prev)
node_1.next=node_2
print(node_1.next)
node_2.prev=node_1
print(node_2.prev)
node_2.next=node_3
print(node_2.next)
node_3.prev=node_2
print(node_3.prev)
node_3.next=node_4
print(node_3.next)
node_4.prev=node_3
print(node_4.prev)
node_4.next=node_5
print(node_4.next)
node_5.prev=node_4
print(node_5.prev)
node_5.next=None
print(node_5.next)
d1.insert_begining("candy crush")
d1.insert_end("hlo")
d1.insert_position(3,"hi")
d1.delete_begining()
d1.delete_end()
d1.delete_pos(3)
d1.display()