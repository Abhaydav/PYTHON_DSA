class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while(True):
            if new_node.value==temp.value:
                return False
            if new_node.value <temp.value:
                if temp.left is None:
                    temp.left =new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
    def contains(self,value):
        if self.root is None:
            return False
        temp=self.root
        while temp is not None:
            if value < temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False
obj=BinarySearchTree()
obj.insert(47)
obj.insert(21)
obj.insert(76)
obj.insert(18)
obj.insert(27)

obj.insert(52)
obj.insert(82)
print(obj.contains(27))

# print(obj.root.value)

# print(obj.root.left.value)

# print(obj.root.right.value)