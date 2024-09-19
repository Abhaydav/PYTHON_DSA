class Node:
    def __init__(self,value):
        self.value=value
        self.next=None



class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    
    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            temp=self.top
            self.top=new_node
            self.top.next=temp 
        self.height+=1
        return True
    def pop(self):
        if self.height==0:
            return None
        temp=self.top
        self.top=temp.next
        temp.next=None
        self.height-=1
        return True
obj=Stack(0)
obj.push(5)
obj.push(6)
obj.push(7)
obj.pop()
obj.print_stack()