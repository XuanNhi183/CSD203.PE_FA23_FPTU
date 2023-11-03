
#Single link list

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next=next
class SingleLinkList:
    def __init__(self) -> None:
        self.head=None
        self.size = 0

    def __len__(self):
        return self.size

    def data(self):
        return self.data
    def addToHead(self,value):
        new_Value = Node(value)  #new_value này có nghĩa là tạo ra 1 cái node mới chứa giá trị value
        if self.head is None:
            self.head = new_Value
            self.size += 1
        else:
            new_Value.next = self.head
            self.head = new_Value
            self.size += 1

    def addToTail(self, value):
        new_value = Node(value)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new_value
        self.size += 1

    def addBefore(self, new_node, index):
        current = self.head
        pos = 1
        while pos < index - 1:
            current = current.next
            pos += 1
        after = current.next
        current.next = new_node
        new_node.next = after
        self.size = self.size + 1

    def addAfter(self, new_node, index):
        pos = 1          #pos là vị trí hiện tại đang xét
        current = self.head
        while pos < index:               #index la vi tri muon chen
            current = current.next
            pos += 1
        after = current.next
        current.next = new_node
        new_node.next = after
        self.size += 1

    def deleteFromHead(self):
        if self.head is None:
            return None
        else:
            p = self.head
            self.head = p.next
            self.size = self.size - 1

    def deleteFromTail(self):
        if self.head is None:
            return None
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
            p.next = None

    def toarray(self):
        list = []
        p = self.head
        while p.next:
            list.append(p.data)
            p = p.next
        print("after to array: ",list)
        return list

    def findMax(self):
        if self.head is None:
            return None
        else:
            p = self.head
            max = p.data
            while p:
                if p.data > max:
                    max = p.data
                p = p.next
            return max

    def findMin(self):
        if self.head is None:
            return None
        else:
            p = self.head
            min = p.data
            while p:
                if p.data < p.data:
                    min = p.data
                p = p.data
            return min

    def sum(self):
        total = 0
        p = self.head
        while p:
            total = total + p.data
            p = p.next
        print("sum = ",total)

    def avg(self):
        sum =0
        p = self.head
        while p:
            sum = sum + p.data
            avg = sum / p.size
            p = p.next
            return avg

#   def avg(self):
#       return self.sum() / self.size

#sort
    def sort(self):
        for i in range (self.size-1,0,1):
            p = self.head
            for j in range (i):
                if p.next.data < p.data:
                    p.next.data = p.data
                p = p.next

    def check_sort(self):
        p = self.head
        while p.next is not None:
            if int(p.data) > int(p.next.data):
                return False
            else:
                p = p.next
        return True

#insert node(x) after the node a
    def add_afterNode(self,index,new_node):
        pos = 1
        while pos < index:
            current = self.head
            pos += 1
        after = current.next
        current.next = new_node
        new_node.next = after
        self.size += 1

    def search(self):
        x = int(input("input your number what you want to find: "))
        p = self.head
        while p:
            if p is None:
                return None
            elif p.data == x:
                print("Found your number what you want to find: ",p.data)
                return True
                p = p.next
            else:
                print("Not found you number what you want to find")
                return False
    def count(self):
        return self.size

    def display(self):
        if self.head is None:
            return None
        else:
            p = self.head
            while p:
                print(p.data, end=' ')
                p = p.next

#----------------------------------------------------------------------------------------------
#Trees
class node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

class BinaryTrees:
    def __init__(self):
        self.root = None
        self.size = 0
        self.total = 0

    def isEmpty(self):
        return self.size == 0
    def count(self):
        return self.size
    def addRoot(self,key):
        new_node = node(key)
        if self.isEmpty():
            self.root = new_node
            self.size += 1
            self.total += new_node.element
        else:
            print("Root is exist")

    def insert(self,p,key):
        if key < p.element:
            if p.left is None:
                new_node = node(key)
                p.left = new_node
                self.size += 1
            if p.left is not None:
               self.insert(p.left,key)

        elif key > p.element:
            if p.right is None:
                new_node = node(key)
                p.right = new_node
                self.size += 1
            if p.right is not None:
                self.insert(p.right,key)

    def search(self,p,key):
        if key < p.element:
            if p.left:
                return self.search(p.left,key)
            else:
                return False
        elif key > p.element:
            if p.right:
                return self.search(p.right,key)
            else:
                return False

        elif key == p.element:
            return True

        else:
            return False

    def preOrder(self,p):  #root -> left -> right
        if p:
            print(p.element,end = " ")
            if p.left:
                self.preOrder(p.left)
            if p.right:
                self.preOrder(p.right)
        else:
            return False

    def inOrder(self,p):   #left -> root -> right
        if p is None:
            return
        self.inOrder(p.left)
        print(p.element, end = " ")
        self.inOrder(p.right)


    def postOrder(self,p):  #left -> right -> root
        if p is None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        print(p.element, end = " ")

    def maxDepth(node):
        if node is None:
            return 0
        else:
            # Compute the depth of each subtree
            lDepth = maxDepth(node.left)
            rDepth = maxDepth(node.right)
            # Use the larger one
            if (lDepth > rDepth):
                return lDepth + 1
            else:
                return rDepth + 1

    def size(node):
        if node is None:
            return 0
        else:
            return (size(node.left) + 1 + size(node.right))

if __name__ == "__main__":
    BStree = BinaryTrees()
    data = [8,13,2,6,7,10,15,1,5,16,17,3]
    BStree.addRoot(data[0])
    for i in data[1:]:
        BStree.insert(BStree.root, i)
    BStree.inOrder(BStree.root)

#------------------------------------------------------------------------------------------------




