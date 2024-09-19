class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None


class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    def pop(self):
       if self.length==0:
        return None
       temp=self.tail
       self.tail=self.tail.prev
       self.tail.next=None
       temp.prev=None
       self.length-=1
    def prepend(self,value):
        new_node=Node(value)
        if self.length ==0:
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.head
            self.head=new_node
            new_node.next=temp
        self.length+=1
        return True
    def pop_first(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            temp.prev=None
        self.length-=1
        return True
    def get(self,index):
        if index <0 or index >= self.length:
            return None
        temp=self.head
        if index <self.length/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length -1,index,-1):
                temp=temp.prev
        return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert(self,index,value):
        
        if index==self.length:
            return self.append(value)
        if index==0:
            return self.prepend(value)
        if index ==self.length:
            return self.append(value)
        new_node=Node(value)
        before=self.get(index-1)
        after=before.next

        new_node.prev=before
        new_node.next=after
        before.next=new_node
        after.prev=new_node
        self.length+=1
        return True
    def remove(self,index):
        if self.length==index:
            return self.pop()
        if index ==0:
            return self.pop_first()
        temp=self.get(index)
        before=temp.prev
        after=temp.next
        before.next=after
        after.prev=before
        return True
        

obj=DoublyLinkedList(0)
obj.append(5)
obj.append(6)
obj.append(7)
# obj.insert(2,8)
obj.remove(2)
# obj.prepend(9)
# obj.pop_first()
# obj.set_value(1,9)
# print(obj.get(3))
obj.print_list()
