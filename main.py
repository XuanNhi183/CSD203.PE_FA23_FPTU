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



if __name__ == "__main__":
    BStree = BinaryTrees()
    data = [8,13,2,6,7,10,15,1,5,16,17,3]
    BStree.addRoot(data[0])
    for i in data[1:]:
        BStree.insert(BStree.root, i)
    BStree.inOrder(BStree.root)