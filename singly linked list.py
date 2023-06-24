class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class SLL:
    def __init__(self):
        self.head= None
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
    def Insert_beginning(self,data):
        new_node=Node(data)#creating a new node
        new_node.next=self.head# pointing the new node (next) to the head node
        self.head=new_node #making new node as the head node
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=None
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node2
    def delete_begining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
    def delete_pos(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
node_1=Node("hlo")
SL=SLL()
SL.head=node_1
node_2=Node("alone")
node_3=Node("single")
node_1.next=node_2
node_2.next=node_3
new_node2=Node("hi")
3#print(node_1.next)
#print(node_2.next)
#print(node_3.next)
SL.Insert_beginning("lakmi")
SL.insert_end("ruthwik")
SL.insert_position(3,"hi")
SL.delete_begining()
SL.delete_end()
SL.delete_pos(2)
SL.display()
#print(SL.head.data)