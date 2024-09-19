class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
        return temp
    def enque(self,value):
        new_node=Node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
        return True
    def dequeue(self):
        if self.length==0:
            return None
        if self.length==1:
            self.first=None
            self.last=None
        temp=self.first
        self.first=temp.next
        temp.next=None
        return True
obj=Queue(0)
obj.enque(1)
obj.enque(2)
obj.enque(3)
obj.dequeue()    #dequeue successfull
obj.print_queue()